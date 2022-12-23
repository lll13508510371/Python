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
for result in results:
    cursor.execute(sql_format % result)
    # cursor.execute("insert into student (no, name, gender, birth, phone, email, address, id_card) values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % ('319001', '赵一', '男', '1998/12/27', '18706012232', '532211428@qq.com', '北京市海淀区颐和园路5号', '342622199801144314'))
# cursor.execute(sql_format % results[1])
# cursor.execute(sql_format % results[2])

conn.commit()
cursor.close()
conn.close()
