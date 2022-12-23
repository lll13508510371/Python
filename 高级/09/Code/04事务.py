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
    # 一条一条数据进行插入
    try:
        print(format_sql % tuple(line.split(',')))
        cursor.execute(format_sql % tuple(line.split(',')))
    except TypeError as e:
        print(e)
        # conn.rollback()  # 回滚, 会把之前提交没有保存修改的内容全部撤销

    # conn.commit()

# 提交修改 删除,修改,插入
conn.commit()
"""
    提交的位置
    在 for 外面进行提交
        只会提交一次

    在 for 里面提交
        每次都会进行提交 提交次数会很多(效率不会那么高)
        每次插入的延时会比较的高
"""
cursor.close()
conn.close()
"""
    插入数据必须提交修改
    
    转账
        银行A  --> 银行B
        转账的操作是一个整体, 要么一起成功, 要么一起失败
"""
