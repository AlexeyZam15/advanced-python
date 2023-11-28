class Count:
    _count = 0
    _last = None

    def __new__(cls, *args, **kwargs):
        if cls._count < 3:
            cls._last = super().__new__(cls)
            cls._count += 1
        return cls._last

    def __init__(self, name: str):
        self.name = name

if __name__ == '__main__':
    c1 = Count('c1')
    c2 = Count('c2')
    c3 = Count('c3')
    c4 = Count('c4')
    print(c1.name)
    print(c2.name)
    print(c3.name)
    print(c4.name)
    print(c3 is c4)
    print(id(c1))
    print(id(c2))
    print(id(c3))
    print(id(c4))
    print(c1._count)
    print(c2._count)
    print(c3._count)
    print(c4._count)
    print(c1._last)
    print(id(c1._last))
