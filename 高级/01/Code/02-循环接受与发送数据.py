import socket

# 1. 创建一个 socket
# socket.AF_INET IPV4 协议的版本
# socket.SOCK_STREAM tcp 协议
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 链接服务器
address = ('127.0.0.1', 7788)
tcp_client_socket.connect(address)

while True:
    # 3. 收发数据
    send_data = input('请输入发送给服务器的数据:')
    # tcp 只能传输二进制的数据
    # 3.1 发送数据
    tcp_client_socket.send(send_data.encode('gbk'))

    # 3.2 接受数据
    recv_data = tcp_client_socket.recv(1024)  # 一次最多接受 1024 B 的数据
    ret = recv_data.decode('gbk')
    print('接受到的数据为:\t', ret)

    # 如果服务器发送欢迎下次光临,客户端就断开链接
    if ret == '欢迎下次光临':
        break

# 4. 断开与服务器的链接
tcp_client_socket.close()
