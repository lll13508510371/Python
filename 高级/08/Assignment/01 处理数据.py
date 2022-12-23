"""
    将 changsha.csv 处理成可以给 sql 直接插入的数据，然后保存到 changsha_result.csv 文件
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

text = open('changsha.csv', mode='r', encoding='gbk').read()

file1 = open('changsha_result.csv', mode='w', encoding='utf-8')

file2 = open('changsha_result.sql', mode='w', encoding='utf-8')
dataset = text.split('\n')
# print(dataset)
for data in dataset[:-1]:
    file1.write(data + '\n')
    print(data)
# for line in dataset[:-1]:
#     # print(line)
#     data = tuple(line.split(','))
#     # print(data)
#     sql_format = "insert into changsha value(0,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');"
#     try:
#         print(sql_format % data)
#         # 这里不能用','连接'\n',write只接受一个参数,用了','就相当于两个参数了
#         file2.write(sql_format % data + '\n')
#     except Exception as e:
#         print('出错了,', e)
file1.close()
file2.close()
