/*
    1. 在远程数据库服务器中创建一个属于自己的数据库：0107_16_01000000（期数-作业次数-学号）
    2. 选择数据库后创建一张 changsha 数据表，字段参考 `01 处理数据.py` 文件
    3. 将处理后的 changsha_result.sql 数据插入到数据库
*/


/*
 [              'city',  # 城市
              'region',  # 行政区
              'title',  # 门店名称
              'star_level',  # 星级
              'star',  # 星级得分
              'review_num',  # 点评总数
              'mean_price',  # 人均消费
              "comment_list1",  # 口味
              "comment_list2",  # 环境
              "comment_list3",  # 环境
              "link",  # 链接网址
              "shop_tag_cate_click",  # 分类
              "shop_tag_region_click",  # 商圈
              "addr",  # 详细地址
              ]
*/
show databases;
create database dzdp character set 'utf8mb4';
use dzdp;
drop table changsha;
create table changsha
(
    id                    int primary key auto_increment,
    city                  varchar(20),
    region                varchar(20),
    title                 varchar(255),
    star_level            varchar(10),
    star                  float,
    review_num            varchar(10),
    mean_price            varchar(10),
    comment_list1         float,
    comment_list2         float,
    comment_list3         float,
    link                  varchar(255),
    shop_tag_cate_click   varchar(255),
    shop_tag_region_click varchar(255),
    addr                  varchar(255)
);
desc changsha;

insert into changsha
values (0, '长沙', '天心区', '盟重烧烤(高正街店)',
        'star_45', 4.74, 8484, '￥74', 4.75, 4.66, 4.56,
        'http://www.dianping.com/shop/l2W3nK2cS8G926v2',
        '烧烤烤串', '天心阁 / 白沙井', '高正街77号（近天心阁社区）');

select * from changsha;

insert into changsha value(0, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');
