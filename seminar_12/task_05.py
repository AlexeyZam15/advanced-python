"""
Доработаем прямоугольник и добавим экономию памяти
для хранения свойств экземпляра без словаря __dict__.
"""
import traceback
from sys import getsizeof


class Rectangle:
    """
    Класс прямоугольник
    """

    __slots__ = ['__length', '__width']

    def __init__(self, length: float, width: float = None):
        """
        Конструктор класса Rectangle
        :param length: длина прямоугольника
        :param width: ширина прямоугольника
        """
        self.__length = None
        self.__width = None

        self.length = length
        if width:
            self.width = width
        else:
            self.width = length

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        if value < 0:
            raise ValueError("Длина не может быть отрицательной")
        self.__length = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("Ширина не может быть отрицательной")
        self.__width = value

    def __str__(self):
        if self.__width != self.__length:
            return f"Прямоугольник со сторонами {self.__length} и {self.__width}"
        return f"Квадрат со стороной {self.__length}"


def try_exec(command):
    try:
        return exec(command)
    except Exception:
        traceback.print_exc()


if __name__ == '__main__':
    rect2 = Rectangle(5)
    try_exec("rect2.__dict__")
    print(rect2.__slots__)
    print(f"{getsizeof(rect2.__slots__) = }")
