/*
    1. 在远程数据库服务器中创建一个属于自己的数据库：0107_16_01000000（期数-作业次数-学号）
    2. 选择数据库后创建一张 changsha 数据表，字段参考 `01 处理数据.py` 文件
    3. 将处理后的 changsha_result.csv 数据插入到数据库
*/
create database 0115_01_15107916 character set 'utf8mb4';

show databases;

use 0115_01_15107916;

/*
字符串和数字可以相互转化,就字符串插入能转化成设置的数字类型(int float double),数字插入能转化成设置的字符串类型(char varchar)
*/
create table changsha
(
    id                    int primary key auto_increment,
    city                  varchar(255),
    region                varchar(255),
    title                 varchar(255),
    star_level            varchar(255),
    star                  float,
    review_num            varchar(255),
    mean_price            varchar(255),
    comment_list1         float,
    comment_list2         float,
    comment_list3         float,
    link                  varchar(255),
    shop_tag_cate_click   varchar(255),
    shop_tag_region_click varchar(255),
    addr                  varchar(255)
);

show tables;

select *
from changsha;

truncate changsha;