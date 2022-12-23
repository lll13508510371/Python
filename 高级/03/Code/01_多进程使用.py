import multiprocessing
import time


def upload():
    print("开始上传文件...")
    time.sleep(1)
    print("完成上传文件...")


def download():
    print("开始下载文件...")
    time.sleep(1)
    print("完成下载文件...")


# upload()
# download()
if __name__ == '__main__':
    # 多进程必须写在 __main__ 下面
    multiprocessing.Process(target=upload).start()
    multiprocessing.Process(target=download).start()
