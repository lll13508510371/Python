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

-- 联想
select brand_name, round(avg(price), 2) as avg_price
from goods
where brand_name = '联想';

select brand_name, round(avg(price), 2) as avg_price
from goods
where brand_name = '苹果';

-- 分组查询
select brand_name, round(avg(price), 2) as avg_price, count(*) as count
from goods
where price > 1000
group by brand_name;


-- 过滤
select brand_name, round(avg(price), 2) as avg_price, count(*) as count
from goods
where price > 1000
group by brand_name
# having avg_price > 4000 -- 过滤查询 将查询出来的结果过滤
having avg_price > 4000 and avg_price < 6000
order by avg_price
;