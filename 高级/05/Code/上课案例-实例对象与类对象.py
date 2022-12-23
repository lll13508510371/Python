class Demo:
    pass
    # __dict__ = {"name": 'Demo'}


class Demo2(Demo):
    def __dict__(self):  # 实例对象的方法
        return {"name": 'Demo2'}


print(Demo2.__dict__)
demo2 = Demo2()
print(demo2.__dict__)
print(demo2.__dict__())
