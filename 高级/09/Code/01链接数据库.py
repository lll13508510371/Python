import pymysql

# 1. 创建链接对象
connection = pymysql.connect(
    user='root',  # 用户名
    password="123456",  # 密码
    host='81.68.68.240',  # 服务器地址
    database='0115_01_15107916',  # 数据库名字
    port=3306,  # 数据库端口
    charset="utf8mb4",  # 字符编码
)
print(connection)

# 2. 获取游标对象执行 sql 指令
cursor = connection.cursor()

# 3. 执行原生 sql 语句
sql = 'show databases;'  # sql 语句
count = cursor.execute(sql)  # 使用游标对象执行 sql 语句
print('执行 sql 之后,受影响的行数:\t', count)

# 4. 获取查询结果
results = cursor.fetchall()
print('查询结果:\t', results)
for result in results:
    print(result[0])

# 5. 关闭与服务器的链接
cursor.close()
connection.close()
