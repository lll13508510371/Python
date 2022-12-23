show databases;
use python;
show tables;
drop table student;
create table student
(
    id      int primary key auto_increment,
    name    VARCHAR(20), -- char 永远占用 20 个字符串, VARCHAR 根据实际的使用长度占据村粗空间
    chinese float,
    phone   char(11),
    birth   DATETIME,
    gender  enum ('男', '女')
);

insert into student(id, name, chinese, phone, birth, gender)
    value (1, '正心', 100, '18675867241', '2000-10-10', '男');

-- id 键不能重复, 可以给 0 设置为默认值
insert into student(id, name, chinese, phone, birth, gender)
    value (0, '正心', 100, '18675867241', '2000-10-10', '男');

-- 某一个字段可以不给, 字段与数据要一一对应
insert into student(name, chinese, phone, birth, gender)
    value ('正心', 100, '18675867241', '2000-10-10', '男');

-- 如果所有字段都给, 可以省略
insert into student
    value (0, '正心', 100, '18675867241', '2000-10-10', '男');


-- 批量插入
insert into student
values (0, '正心', 100, '18675867241', '2000-10-10', '男'),
       (0, '山禾', 100, '18675867241', '2000-10-10', '男'),
       (0, '丸子', 100, '18675867241', '2000-10-10', '男');

select *
from student;