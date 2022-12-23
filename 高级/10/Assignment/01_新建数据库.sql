/*
    将 employee.txt 与 salary.txt 的数据插入到数据库
    1. 使用 .sql 创建数据库, 使用约束与外键约束
    2. 使用 .py 脚本将数据插入到数据库 (--> 使用.py文件将数据插入到数据库)
*/
create
database employee character set utf8mb4;



create table employee
(
    id      int primary key auto_increment,
    name    varchar(20) not null,
    gender  varchar(2) null default '女',
    birth   datetime null, -- 有些关系户进入公司之后才填写一个假的出生如期
    phone   char(11) null,
    email   varchar(20) null,
    address varchar(255),
    id_card char(18),
);


create table employee
(
    id      int primary key auto_increment,
    name    varchar(20) not null,
    gender  char(2) null default '女',
    birth   datetime null,
    phone   char(11) null,
    email   varchar(20) null,
    address varchar(255),
    id_card char(18)
);

drop table
    employee;

use
employee;

drop table
    salary;

create table salary
(
    id           int primary key auto_increment,
    name         varchar(255) not null,
    department   varchar(255) not null,
    job_position varchar(255) not null,
    salary       float,
    employ_id    int,
    constraint employee_id_fk foreign key (employ_id) references employee (id)
);

desc salary;

insert into employee value(0,%s,%s,%s,%s,%s,%s,%s,%s)

desc employee;

select id
from salary
where name = %s

select id
from salary
where name = '周想'
  and salary = 8000

select id
from salary
where name = '周想'