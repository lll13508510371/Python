# 操作路径
import os

print('__file__', __file__)
print(os.path.abspath('.'))
print(os.path.basename(__file__))
print(os.path.dirname(__file__))
print(os.path.split(__file__))
print(os.path.splitext(__file__))

print(os.path.exists('12os.path.py'))  # 判断某个路径是否存在
print(os.path.exists('11sys'))
print(os.path.exists('11sys.py'))
print(os.path.exists('12sys.py'))

# isdir 判断目录是否存在
# isfile 判断文件是否存在
