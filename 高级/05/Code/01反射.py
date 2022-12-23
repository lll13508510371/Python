import math


class Circle:
    def __init__(self, r):
        self.r = r

    def length(self):
        return 2 * math.pi * self.r

    @property
    def area(self):
        return math.pi * self.r ** 2


# dir 查看对象的属性与方法
print(dir(list))
print(dir(Circle))
c1 = Circle(4)
print(dir(c1))
