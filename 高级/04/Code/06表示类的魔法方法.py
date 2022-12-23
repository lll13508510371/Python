import math
import datetime


class Circle:
    """圆"""

    def __init__(self, r):
        self.r = r

    @property
    def area(self):
        # πr²
        return math.pi * self.r ** 2

    def __str__(self):
        # 必须返回字符串
        return f"<class 'Circle' {self.area:.2f}>"


class RectAngle:
    # 正方形
    def __init__(self, width):
        self.width = width

    @property
    def area(self):
        # 正方形的面积
        return self.width * self.width

    def __str__(self):
        return f"<class 'RectAngle'>"


if __name__ == '__main__':
    circle1 = Circle(4)  # 圆
    rect = RectAngle(5)  # 正方形
    print(circle1)
    print(rect)
    print(str(rect))  # str 强制转化的时候会调用 --> __str__
    print(type(datetime.datetime.today()))
    print(datetime.datetime.today())
