import time
import threading
import random

# 1. 创建一把锁
lock = threading.Lock()

number = 0


def add_one():
    global number
    for i in range(1000000):
        # 对敏感数据加锁
        # # 2. 获取一把锁
        # lock.acquire()
        # number += 1
        # # 3. 释放一把锁      # 一定要记得释放这把锁,一旦忘记就会造成死锁
        # lock.release()
        with lock:  # 使用上下文管理器加锁
            number += 1


if __name__ == '__main__':
    threading.Thread(target=add_one).start()
    threading.Thread(target=add_one).start()

    while len(threading.enumerate()) > 1:
        time.sleep(0.5)
    print(number)
