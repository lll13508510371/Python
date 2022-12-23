class AccessCounter(object):
    '''A class that contains a value and implements an access counter.
    The counter increments each time the value is changed.'''
    '''
    统计对象被修改的次数 
    '''

    def __init__(self, val):
        super(AccessCounter, self).__setattr__('counter', 0)
        super(AccessCounter, self).__setattr__('value', val)

    def __setattr__(self, name, value):
        if name == 'value':
            super(AccessCounter, self).__setattr__('counter', self.counter + 1)
        # Make this unconditional.
        # If you want to prevent other attributes to be set, raise AttributeError(name)
        super(AccessCounter, self).__setattr__(name, value)

    def __delattr__(self, name):
        if name == 'value':
            super(AccessCounter, self).__setattr__('counter', self.counter + 1)
        super(AccessCounter, self).__delattr__(name)


if __name__ == '__main__':
    ac = AccessCounter('zx')
    ac.value = '1'
    ac.value = '2'
    print(ac.value)
