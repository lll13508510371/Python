# type 好像还有另一个用法吧？
class X(object):
    a = 1

    def __init__(self, name):
        self.name = name

    def hello(self):
        pass


def hello(self):
    pass


def __init__(self, name):
    self.name = name


X2 = type('X', (object,), {'hello': hello, 'a': 1, '__init__': __init__})
print(X)
print(type(X))
print(X2)
print(type(X2))
# 那个雪花算法是怎么用
