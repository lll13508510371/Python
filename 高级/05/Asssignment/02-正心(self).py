"""
    在 12-02-练习专用 目录下操作
    1. 创建三个文件夹 ['文件夹1', '文件夹2', '文件夹3']
    2. 每个文件夹中随机创建 5-10个.txt 文件，文件夹名用创建时的时间戳命名(延时 0.01 秒创建一个)
    3. 每个文件夹中随机创建 5-10个.py 文件，文件夹名用创建时的时间戳命名
    4. 将 .txt 文件全部复制到 12-02-txt 文件 目录中（没有就自己创建）
    5. 将 .py 文件全部复制到 12-02-py 文件 目录中（没有就自己创建）
"""
import os
import time
import random
import shutil

print(os.getcwd())

os.chdir('D:\\高级\\高级\\05\\Asssignment\\12-02-练习专用')

print(os.getcwd())

folders = ['文件夹1', '文件夹2', '文件夹3']

for i in folders:
    os.chdir('D:\\高级\\高级\\05\\Asssignment\\12-02-练习专用')
    os.mkdir(i)
    os.chdir(i)
    print(os.getcwd())
    file_num = random.randint(5, 10)
    for j in range(file_num):
        time.sleep(0.01)
        file_name = str(time.time())
        with open(file_name + '.txt', mode='w', encoding='utf-8') as f:
            pass
        with open(file_name + '.py', mode='w', encoding='utf-8') as ff:
            pass

# print(os.getcwd())
# os.chdir('D:\\高级\\高级\\05\\Asssignment\\12-02-练习专用\\文件夹1')
# file_list = os.listdir()
# print(file_list)


