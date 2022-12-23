"""
修改 socket 的代码,使 socket 服务器能够同时给多个客户端提供服务

    接收到客户端的请求之后，在 files 目录下创建一个 `{客户端地址}.txt` 的文件，用于记录客户端发过来的所有信息
    与客户端进行通信的时候
        + 记录客户端发送的数据到 `{客户端地址}.txt` 文件中，
        + 发送 `你已经有xx条信息记录` 给客户端（信息数量可以从文件中读取）

"""
import socket
import threading
import time


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.address = (host, port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(128)
        print('服务器启动在:', self.address)

        # 可以接收到很多个用户的请求
        while True:
            socket_client, socket_client_addr = self.socket.accept()

            handle_thread = threading.Thread(target=self.handle_recv, args=(
                socket_client, socket_client_addr))
            handle_thread.start()
            '''
            这里不能把send单独做一个线程,这里是服务器接收到了客户端的数据,服务器再发送消息给客户端,
            是有一个先后顺序的,并不是'同时发生的',所以把send()放入handle_recv()当中调用
            '''
            #
            # send_thread = threading.Thread(target=self.send, args=(
            #     socket_client, socket_client_addr))
            # send_thread.start()

    def handle_recv(self, clt_socket, clt_addr):
        """
        :param clt_socket: 客户端的链接
        :param clt_addr: 客户端的地址
        :return:
        """
        print('客户度的ip地址信息', clt_addr)
        while True:
            recv_data = clt_socket.recv(1024).decode('gbk')
            print(recv_data)
            with open(f'{clt_addr}.txt', mode='a', encoding='utf-8') as f:
                f.write(f'{recv_data}\n')
                '''
                这里用的那个网络调试工具,那个工具没有写\n. 附加内容会附加到同一行当中,所以我在服务器用了\n
                实际上应该是在client用\n,万一客户端发送的消息大于1024byte,就会出现本来是客户端只发送了一条消息,
                结果超过1024byte的内容被第二次接收写入文件下一行当中成为了新的一条消息
                '''
            self.send(clt_socket, clt_addr)
            # print(recv_data.decode('gbk'))
        # 直接发送 hello world ! 回去
        # hello world ！ 能不能从本地文件里面读取出来 ？
        # 文件的名字能不能让客户端传递过来 ？

    def send(self, clt_socket, clt_addr):
        with open(f'{clt_addr}.txt', mode='r', encoding='utf-8') as f:
            data = f.readlines()
            # data_no = str(len(data))
            # f''当中都是字符串, 把len()(int类型)放到f里面得到的结果是str类型
        clt_socket.send(f'你已经有{len(data)}条信息记录'.encode('gbk'))


if __name__ == '__main__':
    serve = Server('127.0.0.1', 7788)
    serve.start()
# 客户端才需要等待
