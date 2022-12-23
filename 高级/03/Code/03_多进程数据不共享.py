import multiprocessing
import threading
import time


def list_append(arr):
    arr.append(1)
    arr.append(2)
    arr.append(3)
    print('arr:\t', arr)


if __name__ == '__main__':
    array = []
    # 普通的添加方式
    # list_append(array)
    # list_append(array)

    # 多线程调用
    # threading.Thread(target=list_append, args=(array,)).start()
    # threading.Thread(target=list_append, args=(array,)).start()

    # 多进程的调用
    multiprocessing.Process(target=list_append, args=(array,)).start()
    multiprocessing.Process(target=list_append, args=(array,)).start()

"""
    多线程数据共享(在同一个进程里面)
    多进程数据不共享(在不同的进程里面完成任务)
    
    多线程是同一条流水线的员工,多进程是两条流水线
"""