import math


class Father:
    pass


class Son(Father):
    pass


# isinstance()  用于判断实例对象
# issubclass()  用于判断子类对象

father = Father()
son = Son()

print(isinstance(son, Son))
print(isinstance(son, Father))

print(isinstance(1, str))
# print(isinstance(True, str))
# print(isinstance([], str))
# print(isinstance([], list))

print('--------判断子类--------')
# 判断子类
print(issubclass(Son, Father))
print(issubclass(int, Father))
