import math


class Circle:
    """圆"""

    def __init__(self, r):
        self.r = r

    @property
    def area(self):
        # πr²
        return math.pi * self.r ** 2

    def equals(self, other):
        return self.area == other.area

    # equal --> eq
    def __eq__(self, other):
        # 重写对象的 == 符号运算
        # return id(self) == id(other)
        return self.area == other.area

    # great than --> gt
    def __gt__(self, other):
        return self.area > other.area


if __name__ == '__main__':
    circle1 = Circle(5)
    circle2 = Circle(5)

    # 比较圆的面积是否相等
    print(circle1.area == circle2.area)
    print(circle1.equals(circle2))

    print(circle1 == circle2)  # 想要判断两个圆的面积是否相等

    # 圆1 > 圆2
    # 想要让对象支持 > 符号的运算, 需要重写底层魔法函数 __gt__
    print(circle1 > circle2)
    print(circle1 < circle2)
    # print(circle1 <= circle2)
    # 魔法函数支持镜像原理 等于/不等于 大于/小于 大于等于/小于等于

# 普通类对象提供了魔法函数的接口,但是没有实现魔法函数的功能
