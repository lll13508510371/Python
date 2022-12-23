class Person:
    def __init__(self, name):
        self.name = name


person = Person('正心')

# 对象.属性 = 属性的值
# person.age = 18
# setattr(实例对象, '属性', 值)
attr1 = 'age'
# attr1 = input('请输入需要设置的属性')
# setattr(person, attr1, 18)

# print(person.age)

attrs = {
    'age': 18,
    'gender': '男'
}

for key, value in attrs.items():
    print(f'key --> {key}')
    # setattr(person, key, value)
    # person.age = value
    # person.gender = value
    # 实际上 key 是一个变量
    person.key = value

print(dir(person))
print(getattr(person, 'key'))
