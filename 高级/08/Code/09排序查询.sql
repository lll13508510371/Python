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

/*  条件查询
    比较运算符   > < >= <= = !=(<>)
    逻辑运算符   &&  ||  !  AND OR NOT
*/
select *
from goods;

-- order by 排序查询
-- 默认为 升序查询(asc) 逆序查询 desc
select price, name, cate_name, brand_name
from goods
where price > 1000
  and price < 8000
order by price desc;


-- 多重排序
-- 先根据品牌排序, 然后再根据价格
select price, name, cate_name, brand_name
from goods
where price > 1000
  and price < 8000
order by brand_name, price;

-- 中文可能根据unicode 编码来排顺序