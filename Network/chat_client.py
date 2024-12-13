# 同样，仅用于测试

import socket
import logging
import threading

FARMAT = "%(asctime)s %(threadName)s %(thread)s %(message)s"
logging.basicConfig(level=logging.INFO, format=FARMAT)


class Chatclient:
    def __init__(self, ip='127.0.0.1', port=9999):
        self.client = socket.socket()
        self.addr = (ip, port)
        self.event = threading.Event()

    def start(self):  # 启动对远端服务器的连接
        self.client.connect(self.addr)
        self.send("I'm ready.")
        # 准备接收数据，recv是阻塞的，开启新的线程
        threading.Thread(target=self.recv, name="recv").start()

    def recv(self):  # 接收服务端的数据
        while not self.event.is_set():
            try:
                data = self.client.recv(1024)  # 阻塞
            except Exception as e:
                logging.error(e)
                break
            msg = "from {}:{} data={}".format(*self.addr, data)
            logging.info(msg)

    def send(self, msg: str):
        data = "{}\n".format(msg.strip()).encode()  # 服务端需要一个换行符
        self.client.send(data)

    def stop(self):
        self.client.close()
        self.event.wait(3)
        self.event.set()
        logging.info('Client stops.')


def main():
    client = Chatclient()
    client.start()
    while True:
        msg = input(">>>")
        client.send(msg)  # 发送信息
        if msg == "quit":
            client.stop()
            break


if __name__ == '__main__':
    main()
