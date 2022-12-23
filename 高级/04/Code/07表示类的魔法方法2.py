import math
import datetime


class Person:
    def __init__(self, name):
        self.name = name

    # def __str__(self):
    #     return f"<Person {self.name}>"

    def __repr__(self):  # 可以在开发调试的时候,修改所有数据容器里面字符串的表达形式
        return f"<Person {self.name}>"


if __name__ == '__main__':
    person = Person('正心')
    arr = [Person(name) for name in ['山禾', '丸子']]
    print(person)
    print(arr)
    print(tuple(arr))
