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
send_data = input('请输入需要下载的文件名')
tcp_client_socket.send(send_data.encode('gbk'))

# recv_data = tcp_client_socket.recv(1024)
# print('服务器:', recv_data)

# 如果文件很大,需要进行多次接受
buffer = []
while True:
    data = tcp_client_socket.recv(1024)  # 每一次接受 1024 b 的数据
    # 每一次接受的数据都是二进制的
    if data:
        buffer.append(data)  # 如果接受到了数据,就添加到缓冲区
    else:
        break  # 接受完了,就调出循环

''' !!!!!! 字符串与二进制的数据不是同一个类型, --必须用二进制的字符串--合并二进制的内容'''
ret = b''.join(buffer)
print(ret)

open('下载内容-' + send_data, mode='wb').write(ret)
# 关闭链接
tcp_client_socket.close()
