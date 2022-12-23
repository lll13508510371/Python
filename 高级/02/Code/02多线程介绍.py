import time
import threading


def work():  # 多线程的任务需要进行打包
    print('5. 洗茶杯：1min')
    time.sleep(1)
    print('6. 放茶叶：1min')
    time.sleep(1)


start_time = time.time()
print('1. 洗壶：1min')
time.sleep(1)
print('2. 灌凉水：1min')
time.sleep(1)
print('3. 烧水：1min')
time.sleep(1)
print('4. 等水烧开：3min')
# 在等待的时候去执行打包好的任务
threading.Thread(target=work).start()  # 创建一个子线程,使用多线程执行任务
time.sleep(1)
time.sleep(1)
time.sleep(1)
# print('5. 洗茶杯：1min')
# time.sleep(1)
# print('6. 放茶叶：1min')
# time.sleep(1)
print('7. 泡茶：1min')
time.sleep(1)
print('总运行时间:\t', time.time() - start_time)

"""
    只要结果没有问题,都是可以的. 代码是非常自由的
"""
