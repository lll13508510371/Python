class Person:
    def __init__(self, name):
        self.name = name


person = Person('正心')

attr1 = 'age'
person.age = 18
setattr(person, 'age', 18)
setattr(person, attr1, 18)
# -------------
setattr(person, 'attr1', 18)
person.attr1 = 18

key = 'age'
value = 'value'
setattr(person, 'key', 'value')
person.key = 'value'
person.key = value

setattr(person, key, 'value')

attrs = {
    'age': 18,
    'gender': '男'
}

for key, value in attrs.items():
    print(f'key :{key} --> value : {value}')

print(getattr(person, attr1), person.age)

# del person.age
# delattr(person, attr1)

if hasattr(person, attr1):
    print('age 为:', getattr(person, attr1))
else:
    print('请先给对象设置属性之后再进行打印')

print(dir(person))
