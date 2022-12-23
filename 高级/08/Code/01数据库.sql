/*
        excel                       sql(mysql/sql server....)
        workbook  一个文件           database  一个数据库
        sheet     一个表             table     一张薄
        列                           字段
        行                           记录
*/


show databases;

-- 创建数据库
-- 创建 数据库 数据库名 字符编码 'utf8mb4';
create database python character set 'utf8mb4';

-- 先选择数据库才能使用
use python;

-- 显示数据表
show tables;
-- sql 语句必须以分号结尾

-- 创建 数据表 数据表名
create table student
(
    id      int primary key auto_increment,
    -- id 字段 int 类型 primary key 主键 auto_increment 自动增长
    name    char(20), -- name 字段 char 字符串 (20) 最大长度为 20
    chinese int,
    math    int,
    english int
);

desc student;
desc STUDENT;
DESC STUDENT;