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
# 1. 准备需要执行的 sql
sql = 'select * from student;'

# 2. 执行 sql --> 返回查询结果(生成器)
count = cursor.execute(sql)
print('受影响的行数:\t', count)

# 3. 获取查询结果
print('获取一条数据:\t', cursor.fetchone())
print('获取多条数据:\t', cursor.fetchmany(4))
print('获取所有数据:\t', cursor.fetchall())

# 如果之前的数据没有获取完,又执行了新的查询,新的查询结果就会覆盖掉旧的
sql = 'select id,no,name,birth from student;'
cursor2.execute(sql)
print('获取所有的数据:\t', cursor2.fetchall())

# 多线程里面执行数据库很容造成覆盖
cursor.close()
conn.close()
