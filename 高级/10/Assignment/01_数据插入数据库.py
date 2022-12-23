# -*- coding: UTF-8 -*-
import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='root',
    database='employee',
    port=3306
)

cursor = conn.cursor()

file1 = open('employee.txt', mode='r', encoding='utf-8').read()
file2 = open('salary.txt', mode='r', encoding='utf-8').read()
# print(file1)
# lines = file1.split('\n')
#
# print(lines)
# array = []
# for line in lines:
#     # print(str(i))
#     record_list = line.split(',')
#     array.append(record_list)
#     # record = tuple(record_list)
#     print(record_list)
# sql = "insert into employee value(0,%s,%s,%s,%s,%s,%s,%s)"
# cursor.executemany(sql, array)
# conn.commit()

sql = 'insert into salary values(0,%s,%s,%s,%s,%s)'
lines2 = file2.split('\n')
for line in lines2:
    # print(str(i))
    record_list = line.split(',')
    print(record_list)
    # record = tuple(record_list)

    salary_id_search = 'select id from employee where name = %s'
    cursor.execute(salary_id_search, (record_list[0],))
    salary_id = cursor.fetchone()[0]
    print(salary_id)
#     cursor.execute(sql, [record_list[0], record_list[1], record_list[2],
#                          record_list[3], salary_id])
#
# # conn.commit()
#
# cursor.close()
# conn.close()

'''
元组 tuple 不能迭代
'''
'''
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
salary 设置外键关联 employee表id就没问题,最终能够成功将数据插入salary表当中
因为外键可以有重复,一对多关系,例如一个作者可以写几本书,!!!!书的表设置外键关联作者表id,对于同一个作者写的书,外键都是一样的(作者id)
------------------------>>>>>>>>>>>>>>>>>>>>>>>
但salary这里是有问题的,因为那两个人名虽然是一样的,但他们不是同一个人,外键显示的都是employee表id 36的那个周想,但salary的 
36 37不是同一个周想 
36,周想,技术部门,前端开发工程师,8000,36
37,周想,技术部门,大前端开发工程师,10000,36
所以这种情况一定要多注意, sql是允许一对多的情况(外键能够重复),但要联系现实情况,像小说作者就是对的,像这里的salary employee就是有问题的
'''
