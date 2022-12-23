import queue
import random
import threading
import time


def producer(pipe):
    index = 1
    while True:
        time.sleep(0.1)
        print(f'厨师做出了 包子 {index}')
        pipe.put(f'包子 {index}')
        index += 1


def consumer(pipe):
    while True:
        time.sleep(random.random())
        item = pipe.get()
        print(f'消费者吃了 {item}')


if __name__ == '__main__':
    pipeline = queue.Queue(maxsize=10)
    # producer(pipeline)
    # consumer(pipeline)
    threading.Thread(target=producer, args=(pipeline,)).start()
    threading.Thread(target=consumer, args=(pipeline,)).start()
    threading.Thread(target=consumer, args=(pipeline,)).start()
