import datetime

from datetime import timedelta

birth_day = datetime.datetime(1949, 10, 1, 0, 0, 0)
one_day = timedelta(days=1)

today = datetime.datetime.today()
print('today:', today)
print('today:', today - one_day * 100)
diff = today - birth_day
print('年', today.year - birth_day.year)
print(diff.days // 365, '年', diff.days % 365, '天')
print(diff.total_seconds())
