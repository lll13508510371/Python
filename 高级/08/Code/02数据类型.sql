show databases;
use python;
show tables;
/*
| 数据类型 | 大小(字节) | 用途             | 格式              |
| -------- | ---------- | ---------------- | ----------------- |
| INT      | 4          | 整数             |                   |
| FLOAT    | 4          | 单精度浮点数     |                   |
| DOUBLE   | 8          | 双精度浮点数     |                   |
| ENUM     | --         | 单选,比如性别    | ENUM('a','b','c') |
| SET      | --         | 多选             | SET('1','2','3')  |
| DATE     | 3          | 日期             | YYYY-MM-DD        |
| TIME     | 3          | 时间点或持续时间 | HH:MM:SS          |
| YEAR     | 1          | 年份值           | YYYY              |
| CHAR     | 0~255      | 定长字符串       |                   |
| VARCHAR  | 0~255      | 变长字符串       |                   |
| TEXT     | 0~65535    | 长文本数据       |                   |
*/
-- CHAR(固定长度字符) VARCHAR(变长字符串)
drop table student;
create table student
(
    id      int primary key auto_increment,
    name    VARCHAR(20), -- char 永远占用 20 个字符串, VARCHAR 根据实际的使用长度占据村粗空间
    chinese float,
    phone   char(11),
    birth   DATETIME,
    gender  enum ('男', '女')
);

-- 查看数据表的结构
desc student;

-- 修改 数据表 数据表明 添加(add) 列(column) 字段名 数据类型;
alter table student
    add column math float after chinese;


--

alter table student
    drop column math;

select *
from student;