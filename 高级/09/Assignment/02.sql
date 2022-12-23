create
database student character set utf8mb4

use student

create table student
(
    id      int primary key auto_increment,
    name    varchar(255),
    chinese int(255),
    math    int(255),
    english int(255)

);

insert into student
values (0, '������', 58, 40, 72),
       (0, '����', 78, 96, 56),
       (0, '����', 99, 64, 84),
       (0, '�����', 75, 92, 43),
       (0, '����', 94, 93, 95),
       (0, '������', 70, 80, 46),
       (0, '����֥', 49, 59, 94),
       (0, '����', 66, 64, 96),
       (0, 'л�㻪', 78, 63, 59),
       (0, '����', 59, 66, 94),
       (0, '����Ӣ', 67, 44, 71),
       (0, '�Ÿ�', 44, 82, 92),
       (0, '³��', 62, 85, 59),
       (0, '�¾�', 53, 51, 81),
       (0, '֣��÷', 51, 72, 57),
       (0, '������', 40, 44, 81),
       (0, '������', 94, 68, 74),
       (0, '�߸�', 95, 89, 74),
       (0, '�ų�', 96, 52, 78)

select *
from student

delete
from student
where name = %s

update student set chinese = %s, math = %s, english = %s where name = %s

select sum(chinese+math+english) from student