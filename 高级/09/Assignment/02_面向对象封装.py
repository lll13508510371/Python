"""
参考 db.py 的逻辑
 + 保留原来的方法，将方法里面的逻辑改成数据库的
 + 新增根据指定科目的成绩大于某个分数的查询的方法（例如：语文分数大于60份的学员）
 + 新增总分大于多少分的查询
"""
import pymysql
import pprint


class MysqlStudentDb:
    def __init__(self):
        self.con = pymysql.connect(
            user='root',
            password='root',
            host='127.0.0.1',
            database='student',
            port=3306,
        )
        self.cursor = self.con.cursor()

    def all(self):
        sql = 'select * from student;'
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def search_by_name(self, name):
        sql = 'select * from student where name = %s;'
        self.cursor.execute(sql, (name,))
        return self.cursor.fetchall()[0]

    # 新增根据指定科目的成绩大于某个分数的查询的方法（例如：语文分数大于60份的学员）
    def search_by_score(self, subject):
        sql = 'select * from student where {} > 60;'.format(subject)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # 新增总分大于多少分的查询
    def search_by_total_score(self):
        sql = 'select * from student where chinese + math + english > 240;'
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    ''' 字符串动态拼接 '''

    def insert(self, student_dic):
        key_str = ''
        value_str = ''
        item_list = list(student_dic.items())
        for key, value in item_list:
            key_str += f'{key},'
            value_str += f"'{value}',"
        keys = key_str.strip(',')
        values = value_str.strip(',')
        print(keys)
        print(values)
        sql = 'insert into student({}) values ({});'.format(keys, values)
        self.cursor.execute(sql)
        self.con.commit()

    def delete_by_name(self, name):
        sql = 'delete from student where name = %s;'
        self.cursor.execute(sql, (name,))
        print('删除成功')

    def update_by_name(self, name, chinese, math, english):
        sql = 'update student set chinese = %s, math = %s, english = %s where name = %s;'
        self.cursor.execute(sql, (chinese, math, english, name))
        print('更新完成')

    def close(self):
        self.cursor.close()
        self.con.close()


if __name__ == '__main__':
    studentdatabase1 = MysqlStudentDb()
    # name = input('请输入想要查询的人名: ')
    # student1 = studentdatabase1.search_by_name(name)
    # print(student1)
    # pprint.pprint(studentdatabase1.search_by_name())

    # student1 = {
    #     'id': 0,
    #     'name': '路',
    #     'chinese': 98,
    #     'math': 97,
    #     'english': 96
    # }
    # studentdatabase1.insert(student1)

    # all_stu = studentdatabase1.all()
    # pprint.pprint(all_stu)

    # name = input('请输入你想要删除的人名: ')
    # studentdatabase1.delete_by_name(name)

    # name = input('请输入你想要更新的人名: ')
    # chinese = input('请输入新的语文成绩: ')
    # math = input('请输入新的数学成绩: ')
    # english = input('请输入新的英语成绩: ')
    # studentdatabase1.update_by_name(name, chinese, math, english)

    # subject = input('请输入想要查询学生的学科: ')
    # students = studentdatabase1.search_by_score(subject)
    # pprint.pprint(students)

    pprint.pprint(studentdatabase1.search_by_total_score())
'''
sql带''插入是不会出错的
'''
