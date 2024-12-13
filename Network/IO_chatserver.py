import threading
import selectors
import socket
import logging

FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


class ChatServer:
    def __init__(self, ip='127.0.0.1', port=9999):
        self.addr = ip, port
        self.sock = socket.socket()
        self.sock.setblocking(False)  # 非阻塞
        self.event = threading.Event()
        self.selector = selectors.DefaultSelector()  # 构建本系统最优Selector

    def start(self):
        self.sock.bind(self.addr)
        self.sock.listen()
        self.selector.register(self.sock, selectors.EVENT_READ, self.accept)  # 注册
        threading.Thread(target=self.select, name='select').start()

    def select(self):
        with self.selector:  # 确保选择器资源正确释放
            while not self.event.is_set():
                events = self.selector.select(0.5)  # 超时0.5秒返回[]
                # 监听注册的对象的事件，发生被关注事件则返回events
                for key, mask in events:
                    key.data(key.fileobj, mask)

    def accept(self, server: socket.socket, mask):
        conn, raddr = server.accept()
        conn.setblocking(False)
        logging.info("New client {} accepted. fd={}".format(raddr, conn.fileno()))
        self.selector.register(conn, selectors.EVENT_READ, self.recv)

    def recv(self, conn: socket.socket, mask):
        data = conn.recv(1024).strip()

        if data == b'' or data == b'quit':
            self.selector.unregister(conn)
            conn.close()  # 关闭前一定要注销
            return
        msg = "Your msg={}".format(data.decode()).encode()
        logging.info(msg)

        for key in self.selector.get_map().values():  # 遍历所有已注册的文件描述符，仅对那些注册了recv方法的客户端发送消息
            print(key.data.__name__)
            # 特别注意，绑定的方法==和is的区别
            print(key.data is self.accept, key.data == self.accept)  # accept：False True；recv：False False
            print(key.data is self.recv, key.data == self.recv)  # accept：False False；recv：False True
            if key.data == self.recv:
                key.fileobj.send(msg)

    def stop(self):
        self.event.set()


if __name__ == '__main__':
    cs = ChatServer()
    cs.start()

    while True:
        cmd = input('>>').strip()
        if cmd == 'quit':
            cs.stop()
            break
        print(*cs.selector.get_map().values())
