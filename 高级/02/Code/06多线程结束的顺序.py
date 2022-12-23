import time
import threading
import random

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


def download(url, index):
    time.sleep(random.random())  # 0~1
    open('ret.txt', mode='a', encoding='utf-8').write(f'{index}:\t' + url + '\n')


start_time = time.time()
index = 1
for url in urls:
    thread_download = threading.Thread(target=download, args=(url, index))
    index += 1
    # thread_download.daemon = True  # 设置为守护线程, 当程序结束的时候会关闭所有的子线程
    thread_download.start()

# 如果主线程结束,子线程就挂掉
print('运行总时间:\t', time.time() - start_time)

"""
    多线程执行任务的时候是没有顺序的  --> 任务执行需要的时间不一样
    需要执行的结果是有顺序的
"""
