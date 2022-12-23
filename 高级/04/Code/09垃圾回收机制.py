class Hero:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        # Hero 对象被销毁之前会自动调用一下 __del__
        print(f'{self.name} 即将被回收')


if __name__ == '__main__':
    hero = Hero('李白')
    hero_back = hero
    input('输入任意内容手动删除 hero:')
    del hero  # del object -->  减少 object 的一次引用, 一旦引用次数为 0 __del__
    try:
        print(hero)
    except Exception as e:
        print('e', e)
    input('输入任意内容,结束程序')
