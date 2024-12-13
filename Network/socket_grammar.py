import socket

server = socket.socket()  # 创建socket对象
server.bind(('127.0.0.1', 9999))  # 一个地址和端口二元组
server.listen()  # 开始监听，等待客户端连接到来，准备accept
print(server)

# 接入一个客户端到来的连接
newsock, raddr = server.accept()  # 阻塞方法，阻塞等待直到有一个客户端连接请求到达。当客户端连接时，它返回一个包含两个元素的元组：新的socket对象 (newsock) 和客户端的地址 (raddr)。newsock是与特定客户端通信的套接字
print(type(newsock), type(raddr))
print(newsock)
print(raddr)
print(newsock.getsockname())  # 获取服务端socket的name
print(newsock.getpeername())  # 获取客户端socket的name
print('-' * 30)

newsock.send(b'hello')  # 服务端向客户端发送数据
data = newsock.recv(1024)  # 服务端接收客户端发送的数据，1024是接收数据的最大长度，返回的是bytes类型，可以用decode()方法解码成字符串，也是一个阻塞方法，当客户端没有发送数据时，会阻塞等待
print(type(data), data)

msg = "data={}".format(data)
newsock.send(msg.encode())  # 服务端向客户端发送数据,要发送的数据必须是bytes类型，所以需要先编码成bytes类型
newsock.close()  # 关闭与特定客户端建立的连接

# 接入另外一个连接
newsock2, raddr2 = server.accept()
data = newsock2.recv(1024)
print(data)
newsock2.close()

server.close()  # 关闭服务器的监听socket，阻止新的连接请求
