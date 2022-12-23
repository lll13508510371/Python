import time
import datetime

"""
    日期
    时间
"""
today = datetime.datetime.today()
print(today)
print(type(today))
print(today.date())
# print(today.year)
# print(today.month)
# print(today.day)
print(today.time())
print(dir(today))
print(int(today.timestamp()))
print(today.strftime("%Y-%m-%d %H:%M:%S"))
a = today.strftime("%Y-%m-%d %H:%M:%S")
print(type(a))
today2 = datetime.datetime.strptime('2022-12-05 01:50:31', "%Y-%m-%d %H:%M:%S")
print('today2', today2)
print(type(today2))
