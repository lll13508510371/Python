import pymysql

conn = pymysql.connect(
    host='81.68.68.240',
    port=3306,
    user='root',
    password='123456',
    database='0115_01_15107916'
)
cursor = conn.cursor()

sql = "select id, no, name, birth from student where name='%s';"
sql_args = "select id, no, name, birth from student where name=%s;"
name = input('请输入查询人的名字:\t')
# sql_backup = sql % name
# print(sql_backup)
# cursor.execute(sql_backup)

# 对查询数据进行参数化
cursor.execute(sql_args, (name,))  # 在进行参数化的时候,会自动的处理 sql 注册
print('获取所有的数据:\t', cursor.fetchall())

"""
    如果使用字符串拼接,就可能会出现 sql 注入
    "赵一" --> "select id, no, name, birth from student where name='赵一';"
    "正心" --> "select id, no, name, birth from student where name='正心';"
    "'or 1=1 or'" --> "select id, no, name, birth from student where name=''or 1=1 or'';"
"""
cursor.close()
conn.close()
