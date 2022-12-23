# -*- coding: utf-8 -*-
import faker
import pymysql

connect = pymysql.connect(
    host='81.68.68.240',
    port=3306,
    user='root',
    password='123456',
    database='0115_01_15107916'
)
cursor = connect.cursor()

create_sql = """
create table user(
    id int primary key auto_increment,
    name varchar(3),
    job varchar(20),
    company varchar(50),
    residence varchar(50),
    blood_group varchar(3),
    username varchar(20),
    sex varchar(1),
    address varchar(50),
    mail varchar(50),
    birthdate varchar(20),
    id_card varchar(18),
    phone varchar(11)
);
"""
cursor.execute(create_sql)
fake = faker.Faker("zh-cn")

"""用户资料详细表"""
for i in range(90):
    data = fake.profile(fields=None, sex=None)
    del data["ssn"]
    del data["website"]
    del data["current_location"]
    data["id_card"] = fake.ssn(min_age=18, max_age=90)
    data["phone"] = fake.phone_number()
    data["birthdate"] = str(data["birthdate"])
    ret = (
        0,
        data["name"],
        data["job"],
        data["company"],
        data["residence"],
        data["blood_group"],
        data["username"],
        data["sex"],
        data["address"],
        data["mail"],
        data["birthdate"],
        data["id_card"],
        data["phone"],
    )

    sql = "insert into user values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    cursor.execute(sql, ret)

connect.commit()
cursor.close()
connect.close()
