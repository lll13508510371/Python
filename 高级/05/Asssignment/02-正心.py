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

target_dir = 'D:\\高级\\高级\\05\Asssignment\\12-02-练习专用'

dir1 = os.path.join(target_dir, '文件夹1')
dir2 = os.path.join(target_dir, '文件夹2')
dir3 = os.path.join(target_dir, '文件夹3')

dir_list = [dir1, dir2, dir3]

for Dir in dir_list:
    if not os.path.exists(Dir):
        os.mkdir(Dir)

for Dir in dir_list:
    file_num = random.randint(5, 10)
    for i in range(file_num):
        '''
        一定要sleep,不然得不到5-10个文件,太快了,如果不sleep,最终可能只能得到2-3个文件
        '''
        time.sleep(0.01)
        # 用了13进制的时间戳
        with open(os.path.join(Dir, f'{int(time.time() * 1000)}.txt'),
                  mode='w', encoding='utf-8') as f:
            pass
        with open(os.path.join(Dir, f'{int(time.time() * 1000)}.py'),
                  mode='w', encoding='utf-8') as ff:
            pass
        '''
        这里可以用多线程的,放假了再试试.
        '''

txt_dir = 'D:\\高级\\高级\\05\Asssignment\\12-02-练习专用\\12-02-txt'
if not os.path.exists(txt_dir):
    os.mkdir(txt_dir)
py_dir = 'D:\\高级\\高级\\05\Asssignment\\12-02-练习专用\\12-02-py'
if not os.path.exists(py_dir):
    os.mkdir(py_dir)

new_file_list = []

for Dir in dir_list:
    old_file_list = os.listdir(Dir)
    # print(old_file_list)
    new_file_list.extend(
        [os.path.join(Dir, file_name) for file_name in old_file_list])
    # print(new_file_list)

    for new_file_path in new_file_list:
        if new_file_path.endswith('.txt'):
            new_file_name = new_file_path.split(os.path.sep)[-1]
            # print(new_file_name)
            shutil.copy(new_file_path, os.path.join(txt_dir, new_file_name))
        elif new_file_path.endswith('.py'):
            new_file_name = new_file_path.split(os.path.sep)[-1]
            # print(new_file_name)
            shutil.copy(new_file_path,
                        os.path.join(py_dir, 'new_file_name.py'))
