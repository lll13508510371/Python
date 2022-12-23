"""
需求
1.在爬取东北三省包括黑龙江，吉林，辽宁三个省所有市县历史 2014年01月至2019年12月 的空气质量指数包括（AQI指数，空气质量状况，PM10，
PM2.5，Co，No2，So2，O3）（http://www.tianqihoubao.com/）
分析：http://www.tianqihoubao.com/lishi/beijing.html

需要的结果如下
['201802', '201803', '201804', ..., '201912', '202001']
"""

import datetime
from dateutil.relativedelta import relativedelta  # 月份相对时间差模块
