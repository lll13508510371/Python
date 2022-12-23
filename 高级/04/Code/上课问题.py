import math


class RectAngle:
    # 正方形
    def __init__(self, width):
        self.width = width

    @property
    def area(self):
        # 正方形的面积
        return self.width * self.width


if __name__ == '__main__':
    rect = RectAngle(5)  # 正方形
    # print(rect.area())  # @property 装饰器可以将实例方法当做实例属性进行调用
    print(rect.area)
