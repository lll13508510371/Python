import time
from datetime import datetime


# !!!age应该是属性        行为
class Person:
    def __init__(self, name, age):
        self.name = name
        # self.age = age
        self.birth = datetime.today().year - age  # 出生年份

    @property  # 特性 计算属性
    def age(self):
        # if self.birth == 0:
        #     raise Exception('年龄已经被删除,无法调用')
        return datetime.today().year - self.birth

    @age.setter
    def age(self, new_age):
        self.birth = datetime.today().year - new_age

    @age.deleter
    def age(self):
        print('self.age 属性需要被删除了')
        # 删除的逻辑没有写 (应该是__del__没写吧,然后age()其实没有被真正删除)
        self.birth = 0


if __name__ == '__main__':
    xl = Person('小丽', 18)
    print(xl.age)
    print(xl.birth)

    '''   过了60 * 60 * 24(一天)之后打印一次   '''
    # while time.sleep(60 * 60 * 24):
    #     print(xl.age())
    #     print(xl.birth)

    # 逻辑有问题,但用来理解@age.setter就够了
    xl.age = 20
    print(xl.birth)
    xl.age = 22
    print(xl.birth)
    del xl.age
    # xl.age
