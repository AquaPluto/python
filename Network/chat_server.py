# 注意，下列代码只为实验用，代码中瑕疵还有很多。Socket太底层了，实际开发中很少使用这么底层的接口。

import socket
import logging
import threading

FARMAT = "%(asctime)s %(threadName)s %(thread)s %(message)s"
logging.basicConfig(level=logging.INFO, format=FARMAT)


class Chatserver:
    def __init__(self, ip='127.0.0.1', port=9999):  # 启动服务
        self.socket = socket.socket()
        self.addr = (ip, port)
        self.clients = {}  # 存储已连接的客户端套接字及其对应的地址信息，实现多客户端之间的消息广播功能
        self.event = threading.Event()
        self.lock = threading.Lock()

    def start(self):  # 启动监听
        self.socket.bind(self.addr)
        self.socket.listen()
        # accept会阻塞主线程，所以开一个新线程
        threading.Thread(target=self.accept, name='accept').start()

    def accept(self):
        """
        监听并接受多个客户端的连接请求。
        此方法通过一个无限循环不断监听新的客户端连接。当有新的连接请求时，
        它接受连接并启动一个新的线程来处理与该客户端的通信，从而实现多客户端的同时处理。
        """
        while not self.event.is_set():
            sock, client = self.socket.accept()
            with self.lock:
                self.clients[client] = sock
            # recv也会阻塞，所以创建一个新的线程以处理与当前客户端的数据接收。
            threading.Thread(target=self.recv, name='recv', args=(sock, client)).start()

    def recv(self, newsocket, client):  # 接收客户端数据
        while not self.event.is_set():
            try:
                data = newsocket.recv(1024)
            except Exception as e:  # 如果出现异常，比如网络中断，直接让服务器端得到空数据，终止接收
                logging.error(e)
                data = b''
            # 客户端退出命令
            if data.decode().strip() == 'quit' or data.decode().strip() == '':  # 客户端主动断开得到空串
                # if data == b'quit' or data == b'':
                with self.lock:
                    self.clients.pop(client)
                    newsocket.close()
                logging.info('{} quits'.format(client))
                break
            msg = "from {}:{} data={}".format(*client, data)
            logging.info(msg)
            with self.lock:
                for s in self.clients.values():
                    s.send(msg.encode())

    def stop(self):  # 关闭服务
        self.event.set()
        with self.lock:
            for s in self.clients.values():
                s.close()
        self.socket.close()


if __name__ == '__main__':
    cs = Chatserver()
    cs.start()
    while True:
        cmd = input(">>>").strip()
        logging.info(threading.enumerate())  # 用来观察断开后线程的变化
        if cmd == "quit":
            cs.stop()
            threading.Event.wait(3)  # 让主线程暂停3秒钟，以便给其他线程足够的时间来完成它们的stop任务
            break
        logging.info(cs.clients)


# 使用makefile改写
class Chatserver:
    def __init__(self, ip='127.0.0.1', port=9999):  # 启动服务
        self.socket = socket.socket()
        self.addr = (ip, port)
        self.clients = {}  # 客户端
        self.event = threading.Event()
        self.lock = threading.Lock()

    def start(self):  # 启动监听
        self.socket.bind(self.addr)
        self.socket.listen()
        # accept会阻塞主线程，所以开一个新线程
        threading.Thread(target=self.accept, name='accept').start()

    def accept(self):
        while not self.event.is_set():
            sock, client = self.socket.accept()
            f = sock.makefile('rw')  # 创建文件对象,支持读写
            with self.lock:
                self.clients[client] = (f, sock)
            # recv也会阻塞，所以创建一个新的线程以处理与当前客户端的数据接收。
            threading.Thread(target=self.recv, name='recv', args=(f, client)).start()

    def recv(self, f, client):  # 接收客户端数据
        while not self.event.is_set():
            try:  # 异常处理
                # data = newsocket.recv(1024)
                data = f.readline().strip()  # 注意readline需要最后加上\n, 否则会一直阻塞
            except Exception as e:
                logging.error(e)
                data = 'quit'
            # 客户端退出命令
            if data == 'quit' or data == '':  # 客户端主动断开得到空串
                with self.lock:
                    f, sock = self.clients.pop(client)
                    sock.close()
                    f.close()
                logging.info('{} quits'.format(client))
                break
            msg = "from {}:{} data={}".format(*client, data)
            logging.info(msg)
            with self.lock:
                for ff, _ in self.clients.values():  # 这里不能跟上面的f同名，否则会覆盖，因为f是局部变量
                    ff.write(msg)
                    ff.flush()

    def stop(self):  # 关闭服务
        self.event.set()
        with self.lock:
            for f, s in self.clients.values():
                s.close()
                f.close()
        self.socket.close()


def main():
    cs = Chatserver()
    cs.start()
    while True:
        cmd = input(">>>").strip()
        logging.info(threading.enumerate())  # 用来观察断开后线程的变化
        if cmd == "quit":
            cs.stop()
            threading.Event.wait(3)  # 让主线程暂停3秒钟，以便给其他线程足够的时间来完成它们的stop任务
            break
        logging.info(cs.clients)


if __name__ == '__main__':
    main()
