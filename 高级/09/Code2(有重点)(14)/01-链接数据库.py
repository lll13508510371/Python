import pymysql

# 1. 创建链接对象
connection = pymysql.connect(
    user='root',  # 用户名
    password='123456',  # 用户密码
    host='81.68.68.240',  # 数据库地址
    port=3306,  # 服务器端口
    database='0115_01_15107916',  # 操作的数据库名
    charset='utf8mb4'
)
print('链接对象:\t', connection)

# 2. 获取游标对象(执行sql指令)
cursor = connection.cursor()

# 3. 执行 sql 指令
sql = 'show databases;'
count = cursor.execute(sql)
print('执行sql之后,受影响的行数:\t', count)

# 4. 获取查询结果
results = cursor.fetchall()
print('查询结果:\t', results)
for result in results:
    print(result)

# 5. 关闭与服务器的链接
cursor.close()
connection.close()
