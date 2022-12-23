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
# 第 30 条数据在保存的时候会少了一个电话号码

# 第 30 条数据出错了, 1-30 条没有提交的数据全部撤销
for result in results:
    try:
        # try 里面有好几条语句,要么一起成功,要么一起失败
        cursor.execute(sql_format % result)
        # conn.commit()
    except Exception as e:
        print('出错啦', e)
        conn.rollback()  # rollback 可以将没有保存到数据库的数据全部撤销更改
'''
正常的数据也会和错误数据一起回滚,这些正常数据不用也很正常,就像10条鱼有一条有病,剩下的九条还要嘛?不要了!
'''
# conn.rollback()
conn.commit()

"""
    插入的操作
    1. execute 执行插入指令  -->  将数据提交到数据库的缓存
    2.1 commit  提交指令     -->  将缓存的数据保存为本地文件(服务器)
    2.2 rollback 撤销指令    -->  撤销对数据的修改

    需要所有的操作全部成功,才能够注册成功 --> 事务 要么一起成功,要么一起失败
        注册用户,填写用户信息
        获取短信验证码
        进行微信验证

操作数据两种方式
    pymysql  +  原生 sql
    使用关系对象模型(ORM) sqlalchemy 直接使用代码操作数据
"""
cursor.close()
conn.close()
