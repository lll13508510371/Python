create database if not exists school character set 'utf8mb4';

use school;
-- 外键约束（选择题，有才可以选择）
drop table if exists student;
drop table if exists teacher;

create table student
(
    id      int primary key auto_increment,
    name    varchar(20),
    subject varchar(20)
);

create table teacher
(
    id     int primary key auto_increment,
    name   varchar(20),
    office varchar(20)
);

create table association
(
    id         int primary key auto_increment,
    student_id int,
    teacher_id int,
    constraint fk_stu_id foreign key (student_id) references student (id),
    constraint fk_tea_id foreign key (teacher_id) references teacher (id)
);

insert into student
values (0, '小红', '文科'),
       (0, '小绿', '文科'),
       (0, '小灰', '理科'),
       (0, '小黑', '理科');

insert into teacher
values (0, '张三', '语文老师'),
       (0, '李四', '历史老师'),
       (0, '王五', '物理老师');

insert into association
values (0, 1, 1),
       (0, 2, 1),
       (0, 3, 1),
       (0, 4, 1),
       (0, 1, 2),
       (0, 2, 2),
       (0, 3, 3),
       (0, 4, 3);

-- 张三老师带了那几个学生

select id
from teacher
where name = '李四';

select student_id
from association
where teacher_id = 2;

select *
from student
where id in (1, 2);

select *
from student;