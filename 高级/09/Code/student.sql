show tables;

# 319001,赵一,男,1998/12/27,18706012232,532211428@qq.com,北京市海淀区颐和园路5号,342622199801144314
use dzdp;
create table student
(
    id      int primary key auto_increment,
    no      varchar(10),
    name    varchar(20),
    gender  char(2),
    birth   datetime,
    mobile  char(11),
    email   varchar(255),
    address varchar(255),
    id_card char(18)
);

desc student;

insert into student value (0, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');

select * from student where name='%s';

update student set birth='2004/01/01',gender='男' where '%s';

select * from student;
truncate student;  -- 清空数据的里面的所有数据
insert into student value (0, '319001', '赵一', '男', '1998/12/27', '18706012232', '532211428@qq.com', '北京市海淀区颐和园路5号', '342622199801144314');
