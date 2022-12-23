"""
参考 db.py 的逻辑
 + 保留原来的方法，将方法里面的逻辑改成数据库的
 + 新增根据指定科目的成绩大于某个分数的查询的方法（例如：语文分数大于60份的学员）
 + 新增总分大于多少分的查询
"""
import pymysql


class MysqlStudentDb:
    def __init__(self):
        self.conn = pymysql.connect(
            user='root',
            password='root',
            host='127.0.0.1',
            database='student',
            port=3306,
        )
        self.cursor = self.conn.cursor()

    def insert(self, student):
        sql = 'insert into student values (0, %s, %s, %s, %s);'
        self.cursor.execute(sql, [student['name'], student['chinese'],
                                  student['math'], student['english']])
        self.conn.commit()

    def all(self):
        sql = 'select * from  student;'
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def search_by_name(self, name):
        sql = 'select * from  student where name=%s;'
        self.cursor.execute(sql, (name,))
        return self.cursor.fetchall()

    def search_score_by_course(self, course, score):
        """
            课程  符号  成绩 --> 对于这种情况,推荐用字符串拼接
            例如 chinese > 60
            参数化只能用于值,不能用于字段(field)
        """
        sql = "select * from student where %s > %s;"
        sql = sql % (course, score)
        '''
        字符串拼接 !!!直接给数字也能转化成字符串(%s)
        用参数化得到的是一个空tuple
        '''
        self.cursor.execute(sql)
        # sql = 'select * from student where %s > %s;'
        # self.cursor.execute(sql, (course, score))
        return self.cursor.fetchall()

    def search_by_total_score(self, total_score):
        sql = 'select * from student where chinese + math + english > %s;'
        self.cursor.execute(sql, (total_score,))
        return self.cursor.fetchall()


db = MysqlStudentDb()

# db.insert({"name": "张三", "math": "65", "chinese": "75", "english": "100"})
# print(db.all())
# print(db.search_by_name('张三'))
print(db.search_score_by_course('chinese', 80))
# print(db.search_score_by_course('math', 80))
# print(db.search_by_total_score(200))
# print(db.update({"name": "张三", "math": "100", "chinese": "100", "english": "100"}))
# print(db.search_by_name('张三'))
# print(db.delete_by_name('张三'))
# print(db.search_by_name('张三'))
