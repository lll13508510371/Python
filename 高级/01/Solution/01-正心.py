# -*- coding: utf-8 -*-
"""
### 作业1：

运行网络调试工具代码，使用 Python 给网络调试工具发送文字信息，并接受网络调试工具发送过来的数据

+ 打开网络调试工具，选择 `tcp` 服务器并启动
+ 编写 Python 代码给 `tcp` 服务器发送一条信息（hello world ！）
+ 之后等待服务器发送一条信息回来并接受打印，然后断开连接

"""
import socket

tcp_socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = ('127.0.0.1', 7788)
tcp_socket_client.connect(address)

recv_data = tcp_socket_client.recv(1024)
print('接收到的数据:\t', recv_data.decode('gbk'))

send_data = input('请输入需要发送给服务器的数据:\t')
tcp_socket_client.send(send_data.encode('gbk'))

tcp_socket_client.close()
