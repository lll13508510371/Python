import time

# 一般用datetime  datetime好用
# 时间戳
print(time.time())

# 结构化对象 struct_time
struct_time_obj = time.localtime()
print(struct_time_obj)
print(time.localtime(1600000000))

# 字符串时间对象
print('2022-12-03 21:32:55')

# 结构化时间对象 转 字符串
print(time.strftime("%Y-%m-%d %H:%M:%S", struct_time_obj))

# 时间戳 转 结构化时间对象
print(time.localtime(1600000000))

# 字符串 转 结构化时间对象
print(time.strptime('2022-12-03 21:32:55', "%Y-%m-%d %H:%M:%S"))

# 结构化时间对象 转 时间戳
print(time.mktime(struct_time_obj))

print('时间戳(10):\t', int(time.time()))
print('时间戳(13):\t', int(time.time() * 1000))
print('时间戳(hex):\t', hex(int(time.time() * 1000)))
