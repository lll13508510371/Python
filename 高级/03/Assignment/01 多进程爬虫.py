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

import multiprocessing
import requests
import time
import concurrent.futures


def get_html(url):
    request = requests.get(url)
    html = request.text
    return html


def save_html(file_name, html):
    with open(file_name, mode='w', encoding='utf-8') as f:
        f.write(html)


def request(url, file_name):
    start_time = time.time()

    html = get_html(url)

    request_time = time.time() - start_time
    # 数据多的时候加一个制表符会好一些 --> 更好查看 --> 不影响观看的时候加不加都无所谓,
    #                                            数据杂乱的时候加上会利于查看数据
    print('请求时间:', request_time)

    save_html(file_name, html)


if __name__ == '__main__':
    # i = 1 要放在for外面,不然每次循环之后i又变回1了
    # 方法一
    i = 1
    executor = concurrent.futures.ProcessPoolExecutor(max_workers=10)
    for Url in baidu_urls:
        # 方法二
        # request_process = multiprocessing.Process(target=request,
        #                                           args=(
        #                                               Url, f'baidu_{i}.html'))
        # request_process.start()
        # i += 1

        executor.submit(request, Url, f'baidu_{i}.html')

        i += 1
'''
多进程请求 baidu_urls ，计算所有请求的时间
题目中计算所有请求时间说的是计算所有线程(各个线程)的请求时间,不是所有线程的请求时间之和
不管对还是错,理解问题的时候最终要有一个自己的想法 --> 要有主见, 不要优柔寡断, 想的过程当中可以往多个点想,想完了之后就不要担心这担心那的
                                              担心有错误之类的,坚持自己最终的想法,不然会很影响效率
'''
