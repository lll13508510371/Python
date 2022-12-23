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
values (0, 'ÀîÓñÕä', 58, 40, 72),
       (0, 'Íõ³¬', 78, 96, 56),
       (0, 'ËÎæÃ', 99, 64, 84),
       (0, 'Îâ¹ğÏã', 75, 92, 43),
       (0, '·¶Åô', 94, 93, 95),
       (0, 'ÖÓÊçÀ¼', 70, 80, 46),
       (0, 'Áõ¹ğÖ¥', 49, 59, 94),
       (0, 'Íõ³©', 66, 64, 96),
       (0, 'Ğ»Ğã»ª', 78, 63, 59),
       (0, 'ÍõÓî', 59, 66, 94),
       (0, '³ÂÀ¼Ó¢', 67, 44, 71),
       (0, '¶Å¸Õ', 44, 82, 92),
       (0, 'Â³³¬', 62, 85, 59),
       (0, '³Â¾²', 53, 51, 81),
       (0, 'Ö£ÓñÃ·', 51, 72, 57),
       (0, '¹ùµ¤µ¤', 40, 44, 81),
       (0, 'ÀîÓñÀ¼', 94, 68, 74),
       (0, '¸ß¸Õ', 95, 89, 74),
       (0, 'ÕÅ³É', 96, 52, 78)

select *
from student

delete
from student
where name = %s

update student set chinese = %s, math = %s, english = %s where name = %s

select sum(chinese+math+english) from student