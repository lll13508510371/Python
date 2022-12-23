import pymysql

conn = pymysql.connect(
    host='81.68.68.240',
    port=3306,
    user='root',
    password='123456',
    database='0115_01_15107916'
)
cursor = conn.cursor()

sql_format = "select * from student where name='%s';"
name = input('请输入需要查询的姓名:\t')
sql = sql_format % name
print('sql --> ', sql)
"""
sql -->  select * from student where name='正心';
sql -->  select * from student where name=''or 1=1 or'';
"""
cursor.execute(sql)
print(cursor.fetchall())

# 修改才需要 commit
cursor.close()
conn.close()
