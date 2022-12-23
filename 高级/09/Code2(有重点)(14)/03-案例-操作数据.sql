show databases;
use 0115_01_15107916;
show tables;

-- 319001,赵一,男,1998/12/27,18706012232,532211428@qq.com,北京市海淀区颐和园路5号,342622199801144314
create table student
(
    id      int primary key auto_increment,
    no      char(6),
    name    varchar(20),
    gender  char(2),
    birth   date,
    phone   char(11),
    email   varchar(50),
    address varchar(255),
    id_card char(18)
);
insert into student
values (0, '319001', '赵一', '男', '1998/12/27', '18706012232', '532211428@qq.com', '北京市海淀区颐和园路5号', '342622199801144314');

insert into student (no, name, gender, birth, phone, email, address, id_card)
values ('319001', '赵一', '男', '1998/12/27', '18706012232', '532211428@qq.com', '北京市海淀区颐和园路5号', '342622199801144314');


insert into student (no, name, gender, birth, phone, email, address, id_card) values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');


select * from student;

truncate student;

select id, no, name, birth from student where name='' or 1=1 or '';

-- 更新与删除必须加限制条件,不然就会修改所有人的信息
update student set name=%s where id=%s;
delete from student where id=%s;


