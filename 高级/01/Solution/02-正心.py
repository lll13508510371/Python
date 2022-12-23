# -*- coding: utf-8 -*-
"""
### 作业2:

将 tcp 文件下载案例中的代码，用面向对象思想进行封装。

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


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.address = (self.host, self.port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # @property  # 计算属性
    # def address(self):
    #     return self.host, self.port

    def start(self):
        self.socket.bind(self.address)
        self.socket.listen(128)
        # 等待客户的链接(阻塞) ? 可以有多少个客户链接
        client_socket, client_address = self.socket.accept()
        # 接受数据(阻塞)
        self.handle_recv(client_socket, client_address)
        # 发送数据(阻塞)
        self.send_file(client_socket, client_address)
        client_socket.close()

    def handle_recv(self, client_socket, client_address):
        # 专门处理客户端的请求
        recv_data = client_socket.recv(1024)
        print('客户端发送过来的消息:\t', recv_data.decode('gbk'))

    def send_file(self, client_socket, client_address):
        send_data = '客户端晚上好'
        client_socket.send(send_data.encode('gbk'))

    def close(self):
        self.socket.close()


if __name__ == '__main__':
    server = Server(host='127.0.0.1', port=7788)
    server.start()
