a, b, c, d, e, f, g = ['a', 'b', 'c', 'd', 'e', 'f', ['g']]

names = [a, b, c, d, e, f, g]
print(names)
# 动态根据变量名生成字段
# {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g'}
# 利用 locals 获取所有的变量名
vk = {}
# 获取局部变量副本 保证不修改局部变量
p_locals = locals().copy()
print('p_locals', p_locals)
# 将内容变为键值对, 并获取id与对象的隐射关系
for k, v in p_locals.items():
    # 用字典值的 id 作为字典的键, 用 key 作为值, 重新构建一个字典
    vk[id(v)] = k
print("vk", vk)

data_dict = {}
for i in names:
    data_dict.update({
        vk[id(i)]: i
    })
# 打印字符串
print(data_dict)

"""
    获取变量名的字符串, 构建字典
"""
