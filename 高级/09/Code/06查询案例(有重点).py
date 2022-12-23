import pymysql

"""  
    用面向对象的方式操作数据库  
    实现对学员数据的增删改查  

    insert    search_by_name    delete_by_name    update_by_name
"""


class Student:
    def __init__(self):
        self.conn = pymysql.connect(
            host='81.68.68.240',
            port=3306,
            user='root',
            password='123456',
            database='0115_01_15107916'
        )
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def insert(self, student):
        sql_format = "insert into student value (0, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');"
        sql = sql_format % student
        self.cursor.execute(sql)
        self.conn.commit()

    def search_by_name(self, name):
        sql_format = "select * from student where name='%s';"
        sql = sql_format % name
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def update_by_name(self, name, info):
        set_item = ''
        # 字符串的动态拼接
        for key, value in info.items():
            set_item += f"{key}='{value}',"
        set_item = set_item.strip(',')
        ''' !!!!! 这个冒号是真搞啊 !!!!!  '''
        sql_format = "update student set " + set_item + " where name='" + name + "';"
        print(sql_format)
        self.cursor.execute(sql_format)
        self.conn.commit()


if __name__ == '__main__':
    student = (
        '319043', '正心', '男', '1996/6/21', '14275603510', '512802414@qq.com',
        '北京市海淀区双清路34号', '340825199806094318')
    db = Student()
    # db.insert(student)
    item = db.search_by_name('正心')
    print(item)
    db.update_by_name('正心', {'birth': '2004/01/01', 'gender': '保密'})
    print(db.search_by_name('正心'))
