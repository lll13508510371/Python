import pymysql

conn = pymysql.connect(
    host='81.68.68.240',
    port=3306,
    user='root',
    password='123456',
    database='0115_01_15107916'
)
cursor = conn.cursor()
cursor2 = conn.cursor()
# 1. 准备需要执行的sql
sql = 'select * from student;'

# 2. 执行 sql  --> 返回的结果是一个生成器
count = cursor.execute(sql)

print('获取一条数据:\t', cursor.fetchone())

# 前面一次的结果没有获取完, 又执行了一次新的查询, 新的会覆盖旧的
cursor2.execute(sql)
print('获取多条数据:\t', cursor.fetchmany(2))
print('获取所有的数据:\t', cursor.fetchall())

print('获取所有的数据:\t', cursor2.fetchall())
cursor.close()
conn.close()

'''
fetchall()返回的是二元元组(元组当中包含元组)
'''
