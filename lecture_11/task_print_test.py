class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = a + b

    def __str__(self):
        return f'MyClass(a={self.a}, b={self.b}, c={self.c})'

    def __repr__(self):
        return str(self.a) + str(self.b) + str(self.c)


if __name__ == '__main__':
    my_obj = MyClass(1, 2)
    print(my_obj)
    print(repr(my_obj))
    print(str(my_obj))
