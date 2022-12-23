import multiprocessing


class Hero:
    def __init__(self, name):
        self.name = name
        print(f'{self.name} 已经被创建了')

    def __del__(self):
        # Hero 对象被销毁之前会自动调用一下 __del__
        print(f'{self.name} 即将被回收')


arr = []


def create_hero():
    hero = Hero('李白')
    arr.append(hero)
    input('输入任意内容结束函数')
    return hero


if __name__ == '__main__':
    # 深浅拷都学了吗 ?
    arr2 = arr
    global_hero = create_hero()
    del global_hero
    # arr2 = []
    arr2[0] = 1
    input('输入任意内容结束程序')

