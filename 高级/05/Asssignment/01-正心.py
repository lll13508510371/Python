"""
    中华人民共和国建国与1949年10月1日，请你计算到今天为止，中国总共成立了多少秒
"""
import datetime

today = datetime.datetime.today()
print(type(today))

birth_time = datetime.datetime(1949, 10, 1, 0, 0, 0)

diff = today - birth_time
print(type(diff))

total_sec = diff.total_seconds()

print(total_sec)
