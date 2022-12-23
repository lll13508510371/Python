import os
import multiprocessing
import threading
import time


def list_append(arr):
    print('os.getpid', os.getpid())
    arr.put(1)
    arr.put(2)
    arr.put(3)
    print('arr:\t', arr.qsize())


if __name__ == '__main__':
    # array = []
    # 普通的添加方式
    # list_append(array)
    # list_append(array)

    # 多线程调用
    # threading.Thread(target=list_append, args=(array,)).start()
    # threading.Thread(target=list_append, args=(array,)).start()

    process_queue = multiprocessing.Queue(maxsize=10)  # 进程队列可以进行数据共享
    # 多进程的调用
    multiprocessing.Process(target=list_append, args=(process_queue,)).start()
    multiprocessing.Process(target=list_append, args=(process_queue,)).start()
    print(os.getpid())
"""
    多线程数据共享(在同一个进程里面)
    多进程数据不共享(在不同的进程里面完成任务)
    
    多线程是同一条流水线的员工,多进程是两条流水线
    
    电脑cpu 8核16进程  物理概念
    
    电脑程序进程数 205 个  逻辑概念
"""