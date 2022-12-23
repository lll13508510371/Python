import time
import threading

urls = [
    'https://maoyan.com/board/4?offset=0',
    'https://maoyan.com/board/4?offset=10',
    'https://maoyan.com/board/4?offset=20',
    'https://maoyan.com/board/4?offset=30',
    'https://maoyan.com/board/4?offset=40',
    'https://maoyan.com/board/4?offset=50',
    'https://maoyan.com/board/4?offset=60',
    'https://maoyan.com/board/4?offset=70',
    'https://maoyan.com/board/4?offset=80',
    'https://maoyan.com/board/4?offset=90',
]


def download(url):
    print('开始下载', url)
    time.sleep(1)
    print('结束下载', url)
    return None


print(threading.enumerate())
start_time = time.time()
for url in urls:
    # download(url)
    # 多线程的作用是将 普通对象(函数对象) 变成多线程对象
    thread_download = threading.Thread(target=download, args=(url,))
    # 启动线程
    thread_download.start()
    print(threading.enumerate())
    # thread_download.join()  # 等待线程执行完之后再继续向下运行

# 打印时间的时候,主线程的任务已经运行完了,但是子线程还在继续工作.
# 主线程默认会等待主线程执行完毕之后才结束

# 等待所有子线程全部运行完毕之后再继续向下执行
# threading.enumerate() 获取当前程序运行的所有线程
while len(threading.enumerate()) > 1:
    # print(threading.enumerate())
    time.sleep(0.5)

print('运行总时间:\t', time.time() - start_time)
