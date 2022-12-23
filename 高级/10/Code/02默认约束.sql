/*
teacher
id	            员工id
name	        员工名字
age	            年龄
salary	        薪水
phone	        电话号码
in_department	所处部门

('刘岩', 50, 2485, '13780795566', '数学'),
('张华', 34, 3707, '13799441431', '数学'),
('王健', 22, 2938, '15055876745', '语文'),
('田丹丹', 51, 3888, '18844659764', '语文'),
('颜秀云', 42, 2148, '18761783434', '数学'),
('胡彬', 38, 3219, '18915977888', '数学'),
('王涛', 24, 2064, '13788639370', '数学'),
('宋琴', 48, 2245, '15208504138', '语文'),
('王杨', 25, 2594, '14568517722', '数学'),
('钟畅', 35, 2710, '14717085283', '语文'),
*/
use python;
show tables;

-- default 默认约束, 如果在给字段的时候不填,就是用默认值
drop table teacher;
create table teacher
(
    id            int primary key auto_increment,
    name          varchar(25),
    age           int,
    salary        float default 2000, -- 薪资如果不填默认就给 2000
    phone         char(11),
    in_department varchar(20)
);

truncate teacher; -- 将所有的数据清空
select *
from teacher;

insert into teacher(id, name, age, salary, phone, in_department)
values (0, '刘岩', 50, 2485, '13780795566', '数学');

insert into teacher(id, name, age, phone, in_department)
values (0, '张华', 34, '13799441431', '数学');

insert into teacher(id, name, salary, phone, in_department)
values (0, '王健', 2938, '15055876745', '语文');

insert into teacher(id, salary, phone, in_department)
values (0, 2938, '15055876745', '语文');