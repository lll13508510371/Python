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

-- 买 4000 以上的电脑
select *
from goods
where price > 4000;
select *
from goods
where price > 8000;
select *
from goods
where price < 4000;

-- 预算在 4000 - 6000
select *
from goods
where price > 4000
  and price < 6000;


-- 预算在 4000 - 6000, 并且想看联想的电脑
select *
from goods
where price > 4000
  and price < 6000
  and brand_name = '联想';


-- 预算在 4000 - 6000, 并且想买联想或者是宏碁的
select *
from goods
where price > 4000 and price < 6000 and brand_name = '联想'
   or brand_name = '宏碁';
select *
from goods
where (price > 4000 and price < 6000 and brand_name = '联想')
   or brand_name = '宏碁';

select *
from goods
where price > 4000
  and price < 6000
  and (brand_name = '联想' or brand_name = '宏碁');

select *
from goods
where price > 4000
  and price < 6000
  and brand_name in ('联想', '宏碁');

-- 只想看宏碁或者是联想的电脑
select *
from goods
where brand_name in ('联想', '宏碁');
