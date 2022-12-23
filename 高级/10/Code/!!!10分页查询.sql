use
dzdp;


select *
from changsha;

/*
SELECT 查询列表
FROM 表
LIMIT (页码-1) * 每页条目个数, 每页条目个数;
*/
select *
from changsha limit 10,10; -- (2-1)*10,10 第 2 页


select *
from changsha limit 90,10;
-- (2-1)*10,10 第 10 页

/*
script 就是一个文件 --> 运行相应的脚步例如运行sql脚本就是运行一个sql文件
*/