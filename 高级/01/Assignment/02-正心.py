# -*- coding: utf-8 -*-
"""
### 作业2:

将tcp文件下载案例中的代码，用面向对象思想进行封装。

1. 服务器（Server）类
    实例属性：
        + 端口、地址、socket

    实例方法：
        - start 启动服务器方法（创建socket、绑定端口、提供服务）
        - handle_recv 处理客户端请求
        - send_file（发送文件方法）

实现两个对象的通信
"""
import socket


class Sever:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.address = (ip, port)
        self.socket = None

    def start(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(self.address)
        self.socket.listen(5)
        print('服务器启动在', self.address)
        client_socket, client_address = self.socket.accept()
        self.handle_recv(client_socket)
        client_socket.close()
        self.socket.close()

    def handle_recv(self, client_socket):
        file_name = client_socket.recv(1024).decode()
        print('服务器接收的数据', file_name)
        self.send_file(client_socket, file_name)

    def send_file(self, client_socket, file_name):
        with open(file_name, mode='rb',) as f:
            content = f.read()

        client_socket.send(content)

if __name__ == '__main__':
    server = Sever('127.0.0.1', 7788)
    server.start()
