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


class RectAngle:
    # 正方形
    def __init__(self, width):
        self.width = width

    @property
    def area(self):
        # 正方形的面积
        return self.width * self.width

    def __add__(self, other):
        # 正方形实现的加法逻辑
        new_area = self.area + other.area
        new_width = math.sqrt(new_area)
        return RectAngle(new_width)


if __name__ == '__main__':
    circle1 = Circle(4)  # 圆
    rect = RectAngle(5)  # 正方形
    new_circle = circle1 + rect
    print(new_circle, new_circle.area)
    new_rect = rect + circle1
    print(new_rect, new_rect.area)

    """
        不同的类如果实现了相同运算规则,就可以直接进行运算
        四则运算: 加减乘数
        逻辑运算: 等于,小于,大于
    """
