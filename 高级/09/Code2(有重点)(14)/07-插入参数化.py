import pymysql

conn = pymysql.connect(
    host='81.68.68.240',
    port=3306,
    user='root',
    password='123456',
    database='0115_01_15107916'
)
cursor = conn.cursor()

text = open('student.txt', mode='r', encoding='utf-8').read()
lines = text.split('\n')
results = []
for line in lines:
    data = tuple(line.split(','))
    results.append(data)

sql_format = "insert into student (no, name, gender, birth, phone, email, address, id_card) values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');"
sql_format_args = "insert into student (no, name, gender, birth, phone, email, address, id_card) values (%s, %s, %s, %s, %s, %s, %s, %s);"
# 插入 40 次
for result in results:
    # cursor.execute(sql_format % result)
    cursor.execute(sql_format_args, result)

# 插入一次
# 参数化的时候可以直接插入多条数据
cursor.executemany(sql_format_args, results)  # executemany 是封装了 execute
conn.commit()
cursor.close()
conn.close()
