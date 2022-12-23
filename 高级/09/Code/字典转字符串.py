info = {'birth': '2004/01/01', 'gender': '保密'}

set_item = ''
# 字符串的动态拼接
for key, value in info.items():
    set_item += f"{key}='{value}',"
set_item = set_item.strip(',')
print(set_item)
