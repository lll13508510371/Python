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

format_sql = "insert into student value (0, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');"

for line in lines:
    # print(line.split(','))
    print(format_sql % tuple(line.split(',')))
    cursor.execute(format_sql % tuple(line.split(',')))
conn.commit()
cursor.close()
conn.close()
