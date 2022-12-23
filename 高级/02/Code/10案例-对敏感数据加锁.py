import time
import threading
import random

lock = threading.Lock()
urls = [
    f'http://www.baidu.com?page={page}' for page in range(100)
]


def download(url, no, name=None):
    # lock.acquire()   # 加锁的时候不能把延时操作也给缩进去,如果把延时操作也给缩进去了,就是顺序执行了
    time.sleep(random.random())  # 大量的时间损耗是延时

    # 文件操作也是一个敏感操作
    # 敏感数据的定义: 共享的数据,同时被多个线程进行操作,可能会出现问题
    # with open('demo.txt', mode='a', encoding='utf-8') as f:
    #     f.write(f'no:{no} name:{name} url:{url}\n')
    lock.acquire()  # 只要对敏感数据加锁就可以了
    with open(f'demo.txt', mode='a', encoding='utf-8') as f:
        f.write(f'no:{no} name:{name} url:{url}\n')
    lock.release()


no = 1
for url in urls:
    # download(url, no, name='百度')
    # 多线程的作用是将普通对象变成多线程对象
    download_thread = threading.Thread(target=download, args=(url, no), kwargs={"name": '百度'})
    download_thread.start()
    no += 1
