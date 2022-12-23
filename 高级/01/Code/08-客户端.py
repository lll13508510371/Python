import socket

# 1. 创建 socket 对象
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('127.0.0.1', 7788)
# 2. 链接服务器
tcp_client_socket.connect(address)

# 3.1 接受服务器的信息
welcome = tcp_client_socket.recv(1024)
print('服务器:', welcome.decode('gbk'))

# 3.2 发送数据给服务器
send_data = input('请输入需要购买的商品')
tcp_client_socket.send(send_data.encode('gbk'))

recv_data = tcp_client_socket.recv(1024)
print('服务器:', recv_data.decode('gbk'))

# 关闭链接
tcp_client_socket.close()
