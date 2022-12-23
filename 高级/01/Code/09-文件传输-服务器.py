import socket

# 1. 创建服务器
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('0.0.0.0', 7788)
# 2. 绑定地址
tcp_server_socket.bind(address)
# 3. 监听客户端的链接
tcp_server_socket.listen(128)
print('正心的文件服务器已经营业')
# 4. 客户端上门
client_socket, client_address = tcp_server_socket.accept()

# 5.1 发送消息给客户端
client_socket.send(f'请输入需要下载的文件名'.encode('gbk'))

# 5.2 接受需要下载的文件名
recv_data = client_socket.recv(1024)
filename = recv_data.decode('gbk')
# 读取文件的数据
content = open(filename, mode='rb').read()

# 将数据发送给客户端
client_socket.send(content)

# 关闭链接
client_socket.close()
tcp_server_socket.close()

# 服务器的逻辑都是写好的,一般不会进行 input

# 语义化
