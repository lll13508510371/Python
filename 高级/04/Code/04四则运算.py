import math


class Circle:
    """圆"""

    def __init__(self, r):
        self.r = r

    @property
    def area(self):
        # πr²
        return math.pi * self.r ** 2

    def length(self):
        # 2πr
        return 2 * math.pi * self.r

    def equals(self, other):
        return self.area == other.area

    def __eq__(self, other):
        return self.area == other.area

    def __gt__(self, other):
        return self.area > other.area

    def __add__(self, other):
        new_area = self.area + other.area
        new_r = math.sqrt(new_area / math.pi)
        return Circle(new_r)


if __name__ == '__main__':
    circle1 = Circle(4)
    circle2 = Circle(5)
    circle3 = Circle(6)

    # # 第一个圆加第二个圆的新圆半径是多少
    # new_area = circle1.area + circle2.area
    # # self.r = math.sqrt(area/math.pi)
    # new_r = math.sqrt(new_area / math.pi)
    # new_circle = Circle(new_r)
    # print(new_circle, new_circle.r, new_circle.area)
    new_circle = circle1 + circle2
    print(new_circle, new_circle.r, new_circle.area)
    new_circle2 = circle1 + circle3 + circle2
    # 从上到下,从左到右
"""
    比较运算的逻辑
    四则运算的逻辑
"""
