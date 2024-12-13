# socketserver模块是对socket编程的封装

# 服务器类：需要提供server_address, RequestHandlerClass参数
# BaseServer
#   +-- TCPServer        # TCP 服务器
#   +-- ThreadingMixIn   # 多线程服务器

# 请求处理类：有request, client_address, server这三个参数
# BaseRequestHandler
#   +-- StreamRequestHandler  # 处理基于流的请求
# 子类需要覆盖setup（连接初始化），handler（请求处理），finish（连接清理）方法

import socketserver
import logging

FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


class MyTCPHandler(socketserver.BaseRequestHandler):  # 继承BaseRequestHandler，调用handle初始化方法
    def handle(self):
        print('=' * 30)
        print(self.request)  # 与客户端通信的new socket
        print(self.client_address)
        print(id(self.server), self.server)
        print('=' * 30)
        for i in range(3):
            data = self.request.recv(1024)
            logging.info(data)
            msg = "from {}:{} data={}".format(*self.client_address, data)
            self.request.send(msg.encode())


server = socketserver.TCPServer(('127.0.0.1', 9999), MyTCPHandler)
print(id(server))  # 和上面的server一样
# server.handle_request()  # 只处理一次请求
server.serve_forever()  # 永久循环执行
server.server_close()  # 关闭
