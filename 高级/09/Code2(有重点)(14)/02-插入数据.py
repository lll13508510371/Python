import pymysql

connection = pymysql.connect(user='root', password='123456',
                             host='81.68.68.240', port=3306,
                             database='0115_01_15107916')

cursor = connection.cursor()
# 数据库中没有对于的数据表,我们该怎么创建 ?
# 对于数据库/数据表的创建删除与修改 放在 .sql 文件里面进行操作
# 对于数据的增删改查,放到 .py 文件里面创建

# 1. 构建插入语句
data = (
'长沙', '天心区', '新疆老马烧烤(碧桂园店)', 'star_35', '3.56', '15', '', '3.56', '3.56',
'3.55',
'http://www.dianping.com/shop/G4YbWvB3PZaTeg2Z', '烤串', '友阿奥特莱斯', '芙蓉南路碧桂园公园壹号')
sql_format = "insert into changsha value (0, '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');"
sql = sql_format % data

# 2. 执行插入操作
cursor.execute(sql)

# 3. 提交保存修改
connection.commit()

cursor.close()
connection.close()
