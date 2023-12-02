"""
Изменяем класс прямоугольника.
Заменяем пару декораторов проверяющих длину и ширину
на дескриптор с валидацией размера.
"""
import traceback
from sys import getsizeof


class Range:
    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = "__" + name

    def __get__(self, instance, owner):
        # return getattr(instance, self.param_name)
        return instance.__dict__[self.param_name]

    def __set__(self, instance, value):
        self.validate(value)
        # setattr(instance, self.param_name, value)
        instance.__dict__[self.param_name] = value

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым числом')
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'Значение {value} должно быть больше или равно {self.min_value}')
        if self.max_value is not None and value >= self.max_value:
            raise ValueError(f'Значение {value} должно быть меньше {self.max_value}')


class Rectangle:
    """
    Класс прямоугольник
    """

    length = Range(0, 10)
    width = Range(0, 10)

    def __init__(self, length: float, width: float = None):
        """
        Конструктор класса Rectangle
        :param length: длина прямоугольника
        :param width: ширина прямоугольника
        """

        self.length = length
        if width:
            self.width = width
        else:
            self.width = length

    def __str__(self):
        if self.width != self.length:
            return f"Прямоугольник со сторонами {self.length} и {self.width}"
        return f"Квадрат со стороной {self.length}"


def try_exec(command):
    try:
        return exec(command)
    except Exception:
        traceback.print_exc()


if __name__ == '__main__':
    rect2 = Rectangle(5)
    print(rect2)
    rect2.width = 4
    print(rect2)
    try_exec("print(rect2.__dict__)")
    print(getsizeof(rect2.__dict__))
    try_exec("del rect2.width")
