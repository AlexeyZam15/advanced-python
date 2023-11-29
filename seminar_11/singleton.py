class Singleton(type):
    instance = None

    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.instance


class MyClass(metaclass=Singleton):
    pass


if __name__ == '__main__':
    s1 = MyClass()
    s2 = MyClass()
    print(s1 is s2)
