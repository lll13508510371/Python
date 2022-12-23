# -*- coding: utf-8 -*-
import concurrent.futures
import time

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def evaluate_item(x):
    """计算总和，这里只是为了消耗时间"""
    a = 0
    for i in range(0, 10000000):
        # 重复计算 消耗时间 cpu计算能力
        a = a + i
    return x


if __name__ == '__main__':
    """单线程"""
    start_time = time.time()
    for item in number_list:
        evaluate_item(item)
    print("单线程执行：" + str(time.time() - start_time), "秒")

    """多线程"""
    start_time_1 = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for item in number_list:
            executor.submit(evaluate_item, item)
    print("线程池计算的时间：" + str(time.time() - start_time_1), "秒")

    """多进程"""
    start_time_2 = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        for item in number_list:
            executor.submit(evaluate_item, item)
    print("进程池计算的时间：" + str(time.time() - start_time_2), "秒")

"""
    理论上 cpu 密集型
    单线程(默认只有一个进程)会比多线程要快,因为多线程会进行任务间的切换,会消耗资源
    多进程会比单进程要快 N (进程的数量,能够稳定运行的情况下) 倍
    
    
    任务:
    io 密集型任务: 执行任务过程中,大量的时间都浪费在等待上
        --> 更适合多线程
        --> 多线程之间的开销小
        --> io 密集型任务速度最快的是 多进程 + 多线程
    
    cpu 密集型任务: 会有大量的计算,多进程切换的开销大
        --> 更适合多进程
        --> 需要更多的 cpu 算力
    
    正则表达式匹配数据               cpu
    往列表里面添加 1 百万个数据       cpu
    向本地文件写入 1000 文件         io(打开与关闭文件) + cpu(写入数据)
    请求 1 万次 百度                io
    
    io 密集型任务的速度瓶颈是网络延时
"""