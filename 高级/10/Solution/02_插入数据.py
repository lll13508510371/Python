import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='root',
    database='company'
)
cursor = conn.cursor()

# sql = 'insert into employee values (0, %s, %s, %s, %s, %s, %s, %s);'
# employee_text = open('employee.txt', mode='r', encoding='utf-8').read()
# results = []
# for line in employee_text.split('\n'):
#     line_data = line.split(',')
#     print(line_data)
#     results.append(line_data)
# cursor.executemany(sql, results)
# conn.commit()

sql = 'insert into salary values (0, %s, %s, %s, %s);'
salary_text = open('salary.txt', mode='r', encoding='utf-8').read()
results = []
for line in salary_text.split('\n'):
    line_data = line.split(',')
    print(line_data)
    employee_search_sql = 'select id from employee where name=%s;'
    cursor.execute(employee_search_sql, line_data[0])
    employee_id = cursor.fetchone()[0]
    cursor.execute(sql,
                   [employee_id, line_data[1], line_data[2], line_data[3]])
conn.commit()
cursor.close()
conn.close()
