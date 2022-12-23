"""
    定义一个等腰直角三角形的模型，求第三边（勾股定理：两直角边的平方和等于斜边的平方a²+b²＝c²）
    模型：Triangle
        属性：侧边（side）
        行为：
            四则运算：两个三角形面积相加，返回一个新的等腰直角三角形
            逻辑运算：两个三角形能进行面积比较
        特性：
            面积（area）
            可以给特性设置面积，然后重新求侧边
"""
import math


class Triangle:
    def __init__(self, side):
        self.side = side

    @property
    def area(self):
        return self.side ** 2 / 2

    def __eq__(self, other):
        return self.area == other.area

    def __add__(self, other):
        new_area = self.area + other.area
        new_side = math.sqrt(2 * new_area)
        return Triangle(new_side)


if __name__ == '__main__':
    triangle1 = Triangle(2)
    triangle2 = Triangle(3)

    triangle3 = triangle1 + triangle2
    print(triangle3)
    print(triangle3.side)
    print(triangle3.area)
    # print(triangle3 > triangle2)
    # print(triangle3 < triangle2)
    print(triangle3 == triangle2)
    print(triangle3.area == triangle2.area)
    print(triangle3.area > triangle2.area)
    print(triangle3.area < triangle2.area)


