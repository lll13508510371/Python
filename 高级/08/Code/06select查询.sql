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

-- 指定字段进行查询
select name, brand_name, price
from goods;

-- 查询字段起别名  as, as 可以省略
select name, brand_name as 'ppm', price 'jg'  -- ppm 品牌名
from goods;

select * from goods;

select brand_name from goods;
-- distinct 对数据进行去重, 查询的结果完全一样才能够去重
select distinct id, brand_name from goods;