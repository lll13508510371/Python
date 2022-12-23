"""
球球大作战

球的属性
    半径
    周长
    面积

需要实现的行为：
    大球吃小球，面积相加，修改原有的球


r 为半径，D 为直径
面积：S=πr²; S=π(d/2）^2
周长：C=πD=2πR
"""
import math


class Circle:
    def __init__(self, r):
        self.r = r
        self.perimeter = 2 * math.pi * r

    '''
    确实,数字要写在前面,不然脑子不灵光的时候以为*写错了,还以为是平方,加了两个**
    '''

    @property
    def area(self):
        return math.pi * self.r ** 2

    # magic method就是实现instances之间的操作
    def __add__(self, other):
        new_area = self.area + other.area
        r = math.sqrt(new_area / math.pi)
        return Circle(r)


# 程序的主入口
if __name__ == '__main__':
    circle1 = Circle(3)
    circle2 = Circle(5)
    circle3 = circle1 + circle2

    print(circle3)
    print(circle3.r)
    print(circle3.area)
    print(circle3.perimeter)
