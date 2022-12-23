import multiprocessing
import time


def run_process(*args, **kwargs):
    print(args, kwargs)


if __name__ == '__main__':
    # 多进程必须写在 __main__ 下面
    multiprocessing.Process(target=run_process, args=(1, 2, 3), kwargs={'a': 'a', 'b': 'b'}).start()
    multiprocessing.Process(target=run_process, args=(4, 5, 6), kwargs={'a': '1', 'b': '2'}).start()
