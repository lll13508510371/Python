# -*- coding: utf-8 -*-
import concurrent.futures
import time
import random

urls = [
    f'https://www.baidu.com?offset={page}' for page in range(1000)
]


def download(url):
    # print(url)
    # 延时从操作
    time.sleep(0.0000001)


# 100 个线程, 每个线程都会下载一张图片, 图片大小为 1mb
# 内存, 网速, cpu性能
if __name__ == '__main__':
    """单线程"""
    start_time = time.time()
    for url in urls:
        download(url)
    print("单线程执行：" + str(time.time() - start_time), "秒")

    """多线程"""
    start_time_1 = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for url in urls:
            executor.submit(download, url)
    print("线程池计算的时间：" + str(time.time() - start_time_1), "秒")

    """多进程"""
    start_time_1 = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        for url in urls:
            executor.submit(download, url)
    print("进程池计算的时间：" + str(time.time() - start_time_1), "秒")

"""
    在 io 密集型任务下, 多线程的速度理论上会比多线程快 N(线程的数量,能够稳定运行的情况下) 倍.
    在 io 密集型任务下, 多线程的速度会比多进程要快. 多进程任务切换开销会比多线程大
    
    自己造轮子,看别人轮子的源码,就需要从底层开始看
"""

