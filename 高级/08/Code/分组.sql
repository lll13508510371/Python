-- 使用 "京东" 数据库
use jingdong;

-- 创建一个商品goods数据表
create table goods
(
    id         int unsigned primary key auto_increment not null,
    name       varchar(150)                            not null,
    cate_name  varchar(40)                             not null,
    brand_name varchar(40)                             not null,
    price      decimal(10, 3)                          not null default 0,
    is_show    bit                                     not null default 1,
    is_saleoff bit                                     not null default 0
);

select *
from goods;

-- 想查询一下每个品牌的平均价格
select distinct brand_name
from goods;



select brand_name, price
from goods
order by brand_name;

select brand_name, avg(price) as avg_price
from goods
where brand_name = '苹果'
order by brand_name;

select brand_name, avg(price) as avg_price
from goods
where brand_name = '戴尔'
order by brand_name;

-- 根据分组条件, 同样的内容会被分到一组
select brand_name, round(avg(price), 2) as avg_price
from goods
group by brand_name;