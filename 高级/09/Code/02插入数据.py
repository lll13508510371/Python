import pymysql

connection = pymysql.connect(user='root', password='123456',
                             host='81.68.68.240', port=3306,
                             database='0115_01_15107916')
cursor = connection.cursor()

# 怎么创建数据表
#   1. pymysql 进行创建数据表 (X)
#   2. 写 .sql 脚本进行创建   (√)

# 插入一条数据
# 需要执行的原生 sql
# sql = "insert into goods values (0, 'ipad mini 配备 retina 显示屏', '平板电脑', '苹果', '2788', default, default);"
# cursor.execute(sql)
# connection.commit()  # 插入数据之后要提交修改

sql = 'update goods set price=1999 where id=1;'
cursor.execute(sql)

sql = 'select * from goods;'
cursor.execute(sql)
results = cursor.fetchall()
print(results)


cursor.close()
connection.close()

"""
CUID
    C create  创建语句一般都是用 .sql 脚本进行操作

    UID 更新 插入 删除 用 pymysql 进行操作
"""