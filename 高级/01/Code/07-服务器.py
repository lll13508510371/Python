import socket

goods = {
    '矿泉水': '2.5 rmb',
    '康师傅冰红茶': '3 rmb',
    '娃哈哈': '1.5 rmb'
}

# 1. 创建服务器
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('0.0.0.0', 7788)
# 2. 绑定地址
tcp_server_socket.bind(address)
# 3. 监听客户端的链接
tcp_server_socket.listen(128)
print('正心的杂货铺已经营业')
# 4. 客户端上门
client_socket, client_address = tcp_server_socket.accept()

# 5.1 发送消息给客户端
client_socket.send(f'欢迎光临正心的杂货铺,现在有以下的一些商品: {list(goods.keys())}'.encode('gbk'))

recv_data = client_socket.recv(1024)
goods_name = recv_data.decode('gbk')
price = goods.get(goods_name, '商品价格不存在')
client_socket.send(f'{goods_name} 的价格为 {price}'.encode('gbk'))

# 关闭链接
client_socket.close()
tcp_server_socket.close()

# 服务器的逻辑都是写好的,一般不会进行 input

# 语义化
