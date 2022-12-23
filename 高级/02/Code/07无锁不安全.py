import time
import threading
import random

number = 0


def add_one():
    global number
    # 运行一百次加 1 运算
    for i in range(1000000):
        number += 1


if __name__ == '__main__':
    threading.Thread(target=add_one).start()
    threading.Thread(target=add_one).start()

    while len(threading.enumerate()) > 1:
        time.sleep(0.5)
    print(number)
