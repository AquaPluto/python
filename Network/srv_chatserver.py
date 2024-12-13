import threading
from socketserver import ThreadingTCPServer, StreamRequestHandler
import logging

FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
lock = threading.Lock()


class ChatHandler(StreamRequestHandler):
    clients = {}  # 用于存储所有已连接客户端的 wfile 对象，以实现消息广播

    def setup(self):
        super().setup()
        self.event = threading.Event()
        with lock:
            self.clients[self.client_address] = self.wfile

    def handle(self):
        super().handle()  # 虽然父类什么都没做，但是调用是个好习惯
        while not self.event.is_set():
            data = self.rfile.readline().strip()  # 从客户端读取数据
            if data == b'quit' or data == b'':
                break
            msg = "From {}:{}. data={}".format(*self.client_address, data)
            with lock:
                for f in self.clients.values():
                    f.write(msg.encode() + b'\n')  # 向客户端发送数据
                    f.flush()  # 刷新缓冲区

    def finish(self):
        with lock:
            self.clients.pop(self.client_address)
        super().finish()
        self.event.set()


class ChatServer:

    def __init__(self, ip='127.0.0.1', port=9999):
        self.server = ThreadingTCPServer((ip, port), ChatHandler)
        self.server.daemon_threads = True

    def start(self):
        threading.Thread(
            target=self.server.serve_forever, name='chatserver', daemon=True).start()

    def stop(self):
        self.server.server_close()


if __name__ == '__main__':
    cs = ChatServer()
    cs.start()
    while True:
        cmd = input('>>').strip()
        if cmd == 'quit':
            cs.stop()
            break
    print(threading.enumerate())
