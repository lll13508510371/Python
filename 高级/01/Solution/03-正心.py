# -*- coding: utf-8 -*-
"""
### 作业3:

2. 客户端（Client）类

    实例属性：
        + 服务器端口、服务器地址、socket

    实例方法：
        + start 启动服务器方法（创建socket、链接服务器）
        + recv_file（发送请求、接收文件方法）
"""
import socket


class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.address = (self.host, self.port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.socket.connect(self.address)
        self.socket.send('服务器晚上好'.encode('gbk'))

        self.recv_file()
        self.socket.close()

    def recv_file(self):
        recv_data = self.socket.recv(1024)
        print('服务发送过来的数据:\t', recv_data.decode('gbk'))


if __name__ == '__main__':
    client = Client('127.0.0.1', 7788)
    client.start()
