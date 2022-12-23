class Person:

    def __new__(cls, *args, **kwargs):
        print('1. __new__ 方法调用了')
        # 需要返回一个最原始的对象
        instance = object.__new__(cls)
        print('instance:', instance)
        return instance

    def __init__(self, name):
        print('2. __init__ 方法调用了')
        print('self:', self)
        # 创建实例对象的时候会自动调用初始化方法
        # self 实例对象
        self.name = name

    def __del__(self):
        print('3. __del__ 方法调用了')

    def say(self):
        return f'{self.name}'


if __name__ == '__main__':
    # 魔法函数是面向对象的底层原理
    person = Person('正心')
    print(person)

"""
    __new__     从哪里来 --> 根据类对象模板创建一个实例对象
    __init__    我是谁   --> 对实例对象进程初始化操作
    __del__     到哪里去 -->  对象在内存里面删除的时候会自动调用
    
    '''
    magic methods 直接是针对实例对象来进行处理
    '''
"""
