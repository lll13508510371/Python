import threading
import time
import concurrent.futures

urls = ['http://www.baidu.com?page={}'.format(page) for page in range(1, 101)]


def download(url):
    print(url)
    time.sleep(1)


# 100 个任务
# for url in urls:
#     download(url)


# 5线程 每个线程 20 个任务
def thread_poll_download(urls):
    # 创建一个线程池
    thread_poll = concurrent.futures.ThreadPoolExecutor(max_workers=5)
    for url in urls:
        thread_poll.submit(download, url)


# thread_poll_download(urls)
# 5进程 每个进程 20 个任务

def process_poll_download(urls):
    # 创建一个进程吃
    thread_poll = concurrent.futures.ProcessPoolExecutor(max_workers=5)
    for url in urls:
        thread_poll.submit(download, url)


# 5多进程（每个进程 20 个任务） + 5多线程（每个线程是四个任务）
def process_and_thread_poll(urls):
    # 多进程嵌套多线程
    process_poll = concurrent.futures.ProcessPoolExecutor(max_workers=5)
    # 多进程嵌套多线程, 多进程进行任务分发, 多线程执行任务
    # urls 里面有一百个任务  100 / 5 进程 每个进程 20 个任务
    for i in range(20, 101, 10):
        process_poll.submit(thread_poll_download, urls[i - 20:i + 1])

    # 同时执行 5 线程 * 5 进程


if __name__ == '__main__':
    # process_poll_download(urls)
    process_and_thread_poll(urls)
