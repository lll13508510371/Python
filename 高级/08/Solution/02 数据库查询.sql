use jingdong;

-- 查询 电影名,评分,关注数 为

-- 求所有电影的平均分数
select round(avg(score),2) as avg_score from douban;

-- 显示每部电影的平均粉丝数
select avg(follows) from douban group by video_name;

-- 查询每部电影中评分 最高、最低、平均评分、数量
select video_name,max(price),min(price),avg(price),count(*) from douban group by video_name;

-- 查询所有关注数大于平均关注数的电影，并且按评分降序排序
select round(avg(follows),2) as avg_price from douban;

select * from douban
where price > (select round(avg(follows),2) as avg_price from douban)
order by price desc;
