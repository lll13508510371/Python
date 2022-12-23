import socket
import threading


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
        while True:  # 一个服务器可能给多个客户提供服务
            # 等待客户的链接(阻塞) ? 可以有多少个客户链接
            client_socket, client_address = self.socket.accept()
            print(f'客户端 {client_address} 链接成功')
            # # 接受数据(阻塞)
            # self.handle_recv(client_socket, client_address)
            handle_recv_thread = threading.Thread(target=self.handle_recv, args=(client_socket, client_address))
            handle_recv_thread.start()
            # # 发送数据(阻塞)
            # self.send_file(client_socket, client_address)
            # # client_socket.close()

    def handle_recv(self, client_socket, client_address):
        # 专门处理客户端的请求
        while True:
            recv_data = client_socket.recv(1024)
            print('客户端发送过来的消息:\t', recv_data.decode('gbk'))
            # 智能客服,收到一条数据之后立马回消息
            send_file_thread = threading.Thread(target=self.send_file, args=(client_socket, client_address))
            send_file_thread.start()

    def send_file(self, client_socket, client_address):
        send_data = '客户端晚上好'
        client_socket.send(send_data.encode('gbk'))

    def close(self):
        self.socket.close()


if __name__ == '__main__':
    server = Server(host='127.0.0.1', port=7788)
    server.start()
