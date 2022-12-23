import pprint

name = '正心'
del name
pprint.pprint(globals())  # 全局变量环境


def func():
    number = 10
    pprint.pprint(locals())


func()

object


class Person:
    name = "John"
    age = 36
    country = "norway"

    #
    # # 重写
    def __dict__(self):
        return {'name': self.name}


x = vars(Person)
print('items', {k: v for k, v in x.items() if not k.startswith('__')})
p = Person()
print('---', p.__dict__())
print('---', p.__dict__)
