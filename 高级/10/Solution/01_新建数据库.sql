/*
    将 employee.txt 与 salary.txt 的数据插入到数据库
    1. 使用 .sql 创建数据库, 使用约束与外键约束
    2. 使用 .py 脚本将数据插入到数据库
*/
show databases;
create database company character set 'utf8mb4';
use company;
drop table employee;
-- 丁娜,女,1998/12/27,18706012232,532211428@qq.com,北京市海淀区颐和园路5号,342622199801144314
create table employee
(
    id      int primary key auto_increment,
    name    varchar(20) not null ,
    gender  char(2)     null default '女',
    birth   datetime    null,
    phone   char(11)    null,
    email   varchar(20) null,
    address varchar(255),
    id_card char(18)
);

-- 丁娜,生产部门,生成主管,5000
create table salary
(
    id              int primary key auto_increment,
    employee_id     int,
    department_name varchar(20),
    position        varchar(20),
    salary          float,
    constraint fk_employee_id foreign key (employee_id) references employee (id)
);

insert into employee
values (0, %s, %s, %s, %s, %s, %s, %s);

select *
from employee;

insert into salary
values (0, %s, %s, %s, %s);

select id
from employee
where name = '丁娜';

select *
from salary;

select name, gender, salary
from employee
         inner join salary s on employee.id = s.employee_id
;

select id
from employee
where name = '丁娜'
  and phone = '18706012232';