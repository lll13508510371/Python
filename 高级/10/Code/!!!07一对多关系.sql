use python;

create table author
(
    id    int primary key auto_increment,
    name  varchar(20),
    hobby varchar(20)
);

insert into author
values (1, '烽火戏诸侯', '吃饭'),
       (2, '我吃西红柿', '睡觉'),
       (3, '辰东', '打豆豆');

create table novel
(
    id        int primary key auto_increment,
    title     varchar(25),
    body      text,
    author_id int,
    constraint fk_author_id foreign key (author_id) references author (id)
);

insert into novel
values (0, '剑来', '...', 1),
       (0, '雪中悍刀行', '...', 1),
       (0, '星辰变', '...', 2),
       (0, '沧元图', '...', 2),
       (0, '飞剑问道', '...', 2),
       (0, '圣墟', '...', 3),
       (0, '遮天', '...', 3),
       (0, '完美世界', '...', 3);

select id
from author
where author.name = '烽火戏诸侯';

select *
from novel
where author_id = 1;



select *
from novel
where author_id = (select id from author where author.name = '辰东');

/*
关联外键避免了冗余数据,比如说一个作者可能写了很多本书,如果每一本书都记录了作者信息,就会有
很多冗余数据,用外键就很好地避免了这样的情况
*/