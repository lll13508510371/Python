"""
    将 changsha.csv 处理成可以给 sql 直接插入的数据，然后保存到 changsha_result.sql 文件
"""

fieldnames = ['city',  # 城市
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

with open('changsha.csv', mode='r', encoding='gbk') as file:
    text = file.read()

file = open('changsha_result.sql', mode='w', encoding='utf-8')
lines = text.split('\n')
for line in lines:
    try:
        data = tuple(line.split(','))
        format_sql = "insert into changsha value(0, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');"
        print(format_sql % data)
        file.write(format_sql % data)
        file.write('\n')
    except TypeError as e:
        print(e)
        # 用 csv 文件进行处理
        # 单独进行处理
file.close()

