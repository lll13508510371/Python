class FunctionalList:
    '''A class wrapping a list with some extra functional magic, like head,
    tail, init, last, drop, and take.'''

    '''
    这里设置values=None是为了创建实例对象的时候不会出错
    '''

    def __init__(self, values=None):
        if values is None:
            self.values = []
        else:
            self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        # if key is of invalid type or value, the list values will raise the error
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    def __iter__(self):
        return iter(self.values)

    def __reversed__(self):
        return reversed(self.values)

    def append(self, value):
        self.values.append(value)

    def head(self):
        # get the first element
        return self.values[0]

    def tail(self):
        # get all elements after the first
        return self.values[1:]

    def init(self):
        # get elements up to the last
        return self.values[:-1]

    def last(self):
        # get last element
        return self.values[-1]

    def drop(self, n):
        # get all elements except first n
        return self.values[n:]

    def take(self, n):
        # get first n elements
        return self.values[:n]


if __name__ == '__main__':
    # arr 是一个普通的对象
    arr = FunctionalList()
    print(arr)
    arr.append(1)
    arr.append(2)
    arr.append(3)
    print(arr)
    print(arr[0])  # [0] 对象取值的时候 -->  __getitem__
    print(arr[0:])  # [0:] 对象切片的时候 -->  __getitem__
    arr[-1] = 'a'  # [-1] = 'a' 对象赋值 --> __setitem__

"""
    自定义的一个列表
"""
