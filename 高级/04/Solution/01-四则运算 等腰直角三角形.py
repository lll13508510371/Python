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

    def __add__(self, other):
        new_area = self.area + other.area
        new_side = math.sqrt(new_area * 2)
        return Triangle(new_side)

    @property
    def area(self):
        return self.side * self.side / 2

    def __str__(self):
        return f'<class Triangle: {self.side}>'

    def __gt__(self, other):
        # return self.area > other.area
        return other.area < self.area  # 用什么符号无所谓, 重要的是逻辑要对

    def __lt__(self, other):
        return self.area < other.area

    def __eq__(self, other):
        return other.area == self.area


if __name__ == '__main__':
    t1 = Triangle(3)
    t2 = Triangle(4)
    new_t = t1 + t2
    print(new_t)
    print(t1 > t2)
    # 逻辑运算支持镜像原理
