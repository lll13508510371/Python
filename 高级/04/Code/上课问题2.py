import os
import time
from multiprocessing import Process


class MyProcess(Process):
    def __init__(self, *args, **kwargs):
        super(MyProcess, self).__init__(*args, **kwargs)
        self.start_time = time.time()

    def __del__(self):
        print(f'{os.getpid()} 即将结束,运行时间为:{time.time() - self.start_time}')


def func():
    time.sleep(1)


if __name__ == '__main__':
    MyProcess(target=func).start()
'''
这里计算了两个线程,应该有一个是主进程,有一个是子进程(感觉应该是只有一个进程(子进程)的运行时间)
'''
