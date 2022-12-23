import pymysql

conn = pymysql.connect(
    host='81.68.68.240',
    port=3306,
    user='root',
    password='123456',
    database='0115_01_15107916'
)
cursor = conn.cursor()

with open('student.txt', mode='r', encoding='utf-8') as file:
    data = file.read()
lines = data.split('\n')

format_sql = "insert into student values (0, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');"

sql = "insert into student values (0, %s, %s, %s, %s, %s, %s, %s, %s);"
arr = []
for line in lines:
    try:
        # print(format_sql % tuple(line.split(',')))
        # cursor.execute(format_sql % tuple(line.split(',')))
        cursor.execute(sql, line.split(','))  # 多个参数
        arr.append(line.split(','))
    except TypeError as e:
        print(e)

# 一次性执行多条数据插入
cursor.executemany(sql, arr)  # 多个参数

conn.commit()
cursor.close()
conn.close()
'''
!!! 在python中一般用列表或者(字典)来进行参数化插入,如上面的arr列表
'''