import pymysql

conn = pymysql.connect(
    host='81.68.68.240',
    port=3306,
    user='root',
    password='123456',
    database='0115_01_15107916'
)
cursor = conn.cursor()
cursor.execute('select id, no, name, birth, address from student;')
results = cursor.fetchall()

update_sql = 'update student set name=%s where id=%s;'
delete_sql = 'delete from student where id=%s;'
for result in results:
    address = result[-1]
    if '北京市' in address:
        cursor.execute(update_sql, (result[2] + '(未检验)', result[0]))
    if '上海市' in address:
        cursor.execute(delete_sql, (result[0],))

conn.commit()
cursor.close()
conn.close()
