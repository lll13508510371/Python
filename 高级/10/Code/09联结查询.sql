use
school;

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


-- 联结多张表进行操作
select association.id,
       student.name,
       student.subject,
       teacher.office,
       teacher.name
from student
         inner join association on student.id = association.student_id
         inner join teacher on association.teacher_id = teacher.id;
/*
 student.id = association.student_id 代表的是两张表的字段关联起来,不是赋值,这两个字段
 本身就是存在的
*/

select a.id, s.name, s.subject, t.office, t.name
from student as s
         inner join association a on s.id = a.student_id
         inner join teacher t on a.teacher_id = t.id
where s.name = '小红'
;

select a.id, s.name, s.subject, t.office, t.name
from teacher t
         inner join association a on t.id = a.teacher_id
         inner join student s on a.student_id = s.id;

#
sqlalchemy