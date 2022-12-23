import socket

# 1. 创建一个 socket 对象
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 绑定一个地址  (选址)
address = ('127.0.0.1', 7788)  # 0.0.0.0 127.0.0.1 192.168.42.227
tcp_server_socket.bind(address)

# 3. 等待客户端的请求 (营业)
tcp_server_socket.listen(128)  # 参照值 最大可以可以监听多少用户的链接
print('正心的杂货铺已经营业')
# 4. 客户端链接成功
# .accept 专门用来监听客户端的链接, 没产生一个新的监听,都会被捕捉到
# client_socket  用来为这个客户进行服务器连接对象
# client_address  客户端是从那里来的
client_socket, client_address = tcp_server_socket.accept()  # 解包
# 5. 收发数据
# 5.1 发送数据
client_socket.send('欢迎光临正心的杂货铺'.encode('gbk'))

# 5.2 接受数据
recv_data = client_socket.recv(1024)
print(f'接受来自客户端 {client_address}:\t', recv_data.decode('gbk'))

# 6. 断开链接
client_socket.close()  # 断开与客户端的链接
tcp_server_socket.close()  # 关闭服务器
