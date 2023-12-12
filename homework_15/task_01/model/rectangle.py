"""
Задача из homework_13
Добавление логирования и запуска с параметрами из командной строки
"""
from homework_15.task_01.aux_modules.exceptions import *


class Rectangle:
    """
    Класс, представляющий прямоугольник.

    Атрибуты:
    - width (int): ширина прямоугольника
    - height (int): высота прямоугольника

    Методы:
    - perimeter(): вычисляет периметр прямоугольника
    - area(): вычисляет площадь прямоугольника
    - __add__(other): определяет операцию сложения двух прямоугольников
    - __sub__(other): определяет операцию вычитания одного прямоугольника из другого
    - __lt__(other): определяет операцию "меньше" для двух прямоугольников
    - __eq__(other): определяет операцию "равно" для двух прямоугольников
    - __le__(other): определяет операцию "меньше или равно" для двух прямоугольников
    - __str__(): возвращает строковое представление прямоугольника
    - __repr__(): возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта
    """

    def __init__(self, width, height=None, name=None):
        self._name = name
        self.check_width(width)
        self._width = width
        if height is None:
            self._height = width
        else:
            self.check_height(height)
            self._height = height

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # @staticmethod
    # def check_name(name):
    #     for rectangle in Rectangle.rectangles:
    #         if name == rectangle._name:
    #             try:
    #                 raise ValueError
    #             except ValueError:
    #                 raise DuplicateNameError(f"Имя {name} уже используется другим прямоугольником")

    @staticmethod
    def check_width(value):
        try:
            value = int(value)
        except TypeError:
            raise NotIntValueError(f"Ширина должна быть целым числом, а не {value}")
        if value < 0:
            try:
                raise ValueError
            except ValueError:
                raise NegativeValueError(f"Ширина должна быть положительной, а не {value}")

    @staticmethod
    def check_height(value):
        try:
            value = int(value)
        except TypeError:
            raise NotIntValueError(f"Высота должна быть целым числом, а не {value}")
        if value < 0:
            try:
                raise ValueError
            except ValueError:
                raise NegativeValueError(f"Высота должна быть положительной, а не {value}")

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self.check_width(value)
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self.check_height(value)
        self._height = value

    def perimeter(self):
        """
        Вычисляет периметр прямоугольника.

        Возвращает:
        - int: периметр прямоугольника
        """
        res = 2 * (self._width + self._height)
        return res

    def area(self):
        """
        Вычисляет площадь прямоугольника.

        Возвращает:
        - int: площадь прямоугольника
        """
        res = self._width * self._height
        return res

    def __add__(self, other):
        """
        Определяет операцию сложения двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем сложения двух исходных прямоугольников
        """
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter // 2 - width
        res = Rectangle(width, height)
        return res

    def __sub__(self, other):
        """
        Определяет операцию вычитания одного прямоугольника из другого.

        Аргументы:
        - other (Rectangle): вычитаемый прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем вычитания вычитаемого прямоугольника из исходного
        """
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter // 2 - width
        res = Rectangle(width, height)
        return Rectangle(width, height)

    def __lt__(self, other):
        """
        Определяет операцию "меньше" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше площади второго, иначе False
        """
        return self.area() < other.area()

    def __eq__(self, other):
        """
        Определяет операцию "равно" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площади равны, иначе False
        """
        return self.area() == other.area()

    def __le__(self, other):
        """
        Определяет операцию "меньше или равно" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше или равна площади второго, иначе False
        """
        return self.area() <= other.area()

    def __str__(self):
        """
        Возвращает строковое представление прямоугольника.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Прямоугольник {self._name} со сторонами {self._width} и {self._height}"

    def __repr__(self):
        """
        Возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Rectangle({self.name}, {self._width}, {self._height})"
