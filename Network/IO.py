import socket
import selectors
import logging

FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)

server = socket.socket()
server.bind(('127.0.0.1', 9999))
server.listen()
server.setblocking(False)  # 建议所有IO对象非阻塞
selector = selectors.DefaultSelector()  # 创建选择器对象，返回当前平台最有效、性能最高的I/O多路复用实现


def accept(server, mask):
    newsock, raddr = server.accept()  # 接收新连接
    newsock.setblocking(False)
    logging.info('new client socket {} in accept.'.format(newsock))
    selector.register(newsock, selectors.EVENT_READ, recv)  # 注册新连接，因为此时是非阻塞IO，确保在调用recv()之前，套接字确实有数据可读。


def recv(conn, mask):
    data = conn.recv(1024)  # 接收数据
    msg = "Your msg = {} ~~~~".format(data.decode())
    logging.info(msg)
    conn.send(msg.encode())


# 等同于accept()，不同于accept。为selector注册一个文件对象，这里是告诉selector帮忙监控server的读第一阶段就绪（EVENT_READ）
# IO监控只有读和写
# 返回SelectorKey对象，fileobj（文件对象，其实就是server）,fd（文件描述符），events（事件），data（自定义数据）
key = selector.register(server, selectors.EVENT_READ, accept)
logging.info(key)
# SelectorKey(fileobj=<socket.socket fd=384, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 9999)>, fd=384, events=1, data=<function accept at 0x000001D12B997F60>)

while True:
    events = selector.select()  # 阻塞，直到至少有一个文件描述符准备好。在Linux中，select是epoll，因为是一个统一封装好的接口。这行的代码的意思就是我（操作系统）开始盯着注册的IO了，第一阶段
    print(type(events))  # <class 'list'>
    print(events)  # 二元组列表，每个二元组包含两个元素，第一个元素是SelectorKey对象，第二个元素是事件。

    for key, mask in events:
        # 通过data找到你想要的路，比如这里有100路，从里面找想要的路并accept
        callback = key.data
        callback(key.fileobj, mask)  # accept(server, mask)/recv(conn, mask)
