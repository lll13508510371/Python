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
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.address = (ip, port)
        self.socket = None

    def start(self, family, type):
        self.socket = socket.socket(family, type)
        self.socket.connect(self.address)
        self.recv_file()
        self.socket.close()

    def recv_file(self):
        filename = input('请输入向服务器请求的文件名称:')
        self.socket.send(filename.encode())
        while True:
            data = self.socket.recv(1024)
            with open('[下载]' + filename, mode='ab') as f:
                f.write(data)
            if not data:
                break
            '''
            如果没有接收到数据,data就是False, not data这个时候就是 not False,
            也就是True, 执行break
            '''
            '''
            if, while 条件都要满足为True才会执行   if not也是--> if not i == 1(if i !=1)  
            或者 if not False(if True)
            '''

            '''
        # while True:
        #     data = self.socket.recv(1024)
        #     if data:
        #         with open('[下载]' + filename, mode='ab') as f:
        #             f.write(data)
        #     # 如果没有接收到数据 data = None
        #     else:
        #         break
            '''


if __name__ == '__main__':
    client = Client('127.0.0.1', 7788)
    client.start(socket.AF_INET, socket.SOCK_STREAM)
