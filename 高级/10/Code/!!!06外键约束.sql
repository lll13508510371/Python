create
database if not exists school character set 'utf8mb4';

use
school;
-- 外键约束（选择题，有才可以选择）
drop table if exists student;
drop table if exists teacher;

create TABLE teacher
(
    id            INT PRIMARY KEY AUTO_INCREMENT,
    name          varchar(20),
    age           int,
    salary        float,
    phone         char(11),
    in_department varchar(20)
) character set utf8;


-- 插入三条数据
insert into teacher(name, age, salary, phone, in_department)
values ('刘岩', 50, 2485, '13780795566', '数学'),
       ('张华', 34, 3707, '13799441431', '数学'),
       ('王健', 22, 2938, '15055876745', '语文');


-- 插入学生信息时, 老师必须存在于 teacher 表里面
create table student
(
    id         int primary key auto_increment,
    name       varchar(20) not null,
    math       int,
    chinese    int,
    english    int,
    teacher_id varchar(20),
    constraint fk_teacher_id foreign key (teacher_id) references teacher (id)
);

-- 插入学生信息时，学生的老师名字填写错了
insert into school.student(name, math, chinese, english, teacher_id)
values ('胡秀英', 77, 75, 51, 2),
       ('李玉珍', 58, 40, 72, 1),
       ('王超', 78, 96, 56, 3);

insert into school.student(name, math, chinese, english, teacher_id)
values ('宋婷', 99, 64, 84, 4);
/*
    插入学生信息时, 老师必须存在于老师表里面
*/

desc student;

/*
外键约束 constraint 就是没有的数据是插不进表里面的,我是这么理解的
*/