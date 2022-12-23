import time
import threading


def download():
    print("开始下载文件...")
    time.sleep(1)
    print("完成下载文件...")


def upload():
    print("开始上传文件...")
    time.sleep(1)
    print("完成上传文件...")


# download()
# upload()

thread_download = threading.Thread(target=download)
thread_download.start()
thread_upload = threading.Thread(target=upload)
thread_upload.start()
