"""
球球大作战

球的属性
    半径
    周长
    面积

需要实现的行为：
    大球吃小球，面积相加，修改原有的球


r 为班级，D 为直径
面积：S=πr²; S=π(d/2）^2
周长：C=πD=2πR
"""
import math


class Circle:
    def __init__(self, r):
        self.r = r

    def length(self):
        return 2 * math.pi * self.r

    @property
    def area(self):
        return math.pi * self.r ** 2

    def __str__(self):
        return f'<Circle area: {self.area:.2f}>'

    def __add__(self, other):
        new_area = self.area + other.area
        new_r = math.sqrt(new_area / math.pi)
        self.r = new_r
        other.r = 0
        # return self

    def __gt__(self, other):
        return self.area > other.area


if __name__ == '__main__':
    c1 = Circle(5)
    c2 = Circle(6)
    print('c2', c2)
    if c2 > c1:
        c2 + c1
    else:
        c1 + c2
        # 谁在前面,改变的就是谁
    print('c2', c2)
    print('c1', c1)
