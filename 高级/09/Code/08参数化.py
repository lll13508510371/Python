import pymysql

conn = pymysql.connect(
    host='81.68.68.240',
    port=3306,
    user='root',
    password='123456',
    database='0115_01_15107916'
)
cursor = conn.cursor()
# 可以用参数化解决 sql 注入
# 1. 需要将 %s 两端的字符串去掉
sql_format = "select * from student where name=%s;"
name = input('请输入需要查询的姓名:\t')
# 2. 在执行 sql 的时候传入参数
cursor.execute(sql_format, name)
print(cursor.fetchall())

cursor.close()
conn.close()

"""
动态拼接加单引号，参数不用加单引号
"""