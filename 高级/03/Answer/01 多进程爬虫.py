# import multiprocessing
import concurrent.futures
import time
import os

baidu_urls = ['https://www.baidu.com/', 'https://www.baidu.com/',
              'https://www.baidu.com/', 'https://www.baidu.com/',
              'https://www.baidu.com/', 'https://www.baidu.com/',
              'https://www.baidu.com/', 'https://www.baidu.com/',
              'https://www.baidu.com/', 'https://www.baidu.com/']

""" 
    定义一个请求方法 get_html 用于并返回网页数据
    定义一个保存方法 save_html 用于保存返回的网页数据
    
    多进程请求 baidu_urls ，计算所有请求的时间
    然后去将每一个文件分别标号保存，保存文件名为
    baidu_1.html,baidu_2.html,baidu_3.html,
    baidu_4.html,baidu_5.html,baidu_6.html,
    baidu_7.html,baidu_8.html,baidu_9.html,
    baidu_10.html


如果不会爬虫, 可以参照下面的请求，也可以微信私聊正心
>>> import requests
>>> response = requests.get('https://www.baidu.com/')
>>> html = response.text
"""
import requests


def get_html(url):
    response = requests.get(url)
    html = response.text
    return html


def save_html(html, name):
    with open(name, mode='w', encoding='utf-8') as file:
        file.write(html)


def main(url, name, start_time):
    html = get_html(url)
    save_html(html, name)
    print(f'进程{os.getpid()} 运行的时间:\t', time.time() - start_time)




if __name__ == '__main__':

    # baidu_1.html
    main_start_time = time.time()
    process_poll = concurrent.futures.ProcessPoolExecutor(max_workers=5)
    index = 1
    for url in baidu_urls:
        # html = get_html(url)
        # save_html(html, 'baidu_{}.html'.format(index))
        # main(url, 'baidu_{}.html'.format(index))
        # 多线程的作用是将普通对象编程多线程对象
        start_time = time.time()
        process_poll.submit(main, url, 'baidu_{}.html'.format(index), start_time)

        # process_poll.submit(main, url)  # 可能不会报错,是被多进程内部处理了
        index += 1
    process_poll.shutdown()  # 等待所有子进程运行完毕
    print(f'主进程{os.getpid()} 运行的时间:\t', time.time() - main_start_time)