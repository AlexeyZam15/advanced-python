"""
Задача из homework_13
Добавление логирования и запуска с параметрами из командной строки
"""
import logging
import argparse
import sys


class MyBaseException(Exception):
    def __init__(self, string):
        self.str = string
        exc_type, exc_obj, exc_tb = sys.exc_info()
        self.error_line = exc_tb.tb_lineno
        super().__init__(self.str)


class NegativeValueError(MyBaseException):
    pass


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

    def __init__(self, width, height=None):
        self.check_width(width)
        self._width = width
        if height is None:
            self._height = width
        else:
            self.check_height(height)
            self._height = height
        logger.info(f" - Инициализирован экземпляр класса {self.__class__.__name__} - {self}")

    @staticmethod
    def check_width(width):
        if width < 0:
            try:
                raise ValueError
            except ValueError:
                raise NegativeValueError(f"Ширина должна быть положительной, а не {width}")

    @staticmethod
    def check_height(height):
        if height < 0:
            try:
                raise ValueError
            except ValueError:
                raise NegativeValueError(f"Высота должна быть положительной, а не {height}")

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self.check_width(value)
        logger.info(f" - ширина прямоугольника {repr(self)} изменена на {value}")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self.check_height(value)
        logger.info(f" - высота прямоугольника {repr(self)} изменена на {value}")
        self._height = value

    def perimeter(self):
        """
        Вычисляет периметр прямоугольника.

        Возвращает:
        - int: периметр прямоугольника
        """
        res = 2 * (self._width + self._height)
        logger.info(f"Вычислен периметр прямоугольника {repr(self)}: {res}")
        return res

    def area(self):
        """
        Вычисляет площадь прямоугольника.

        Возвращает:
        - int: площадь прямоугольника
        """
        res = self._width * self._height
        logger.info(f"Вычислена площадь прямоугольника {repr(self)}: {res}")
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
        logger.info(f"Выполнена операция сложения {repr(self)} и {repr(other)}. Получился прямоугольник {repr(res)}")
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
        logger.info(f"Выполнена операция вычитания {repr(self)} и {repr(other)}. Получился прямоугольник {repr(res)}")
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
        return f"Прямоугольник со сторонами {self._width} и {self._height}"

    def __repr__(self):
        """
        Возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Rectangle({self._width}, {self._height})"


def try_exec(*commands):
    for command in commands:
        command_string = command.split('\n')
        for command_s in command_string:
            try:
                print(f"Команда:\n{command_s}", "\n", "_" * 60)
                logger.info(f" - Выполнение команды: {command_s}")
                exec(command_s)
            except MyBaseException as e:
                print(f"{e.__class__.__name__}: {e}")
                logger.error(
                    f" - Выполнение команды {command_s} завершилось ошибкой: '{e.__class__.__name__}: {e}' - строка ошибки: {e.error_line}")
            print()


if __name__ == '__main__':
    file_name = __file__.split("\\")[-1]

    logger = logging.getLogger(file_name)

    FORMAT = 'уровень логирования: {levelname} - дата события: {asctime} - имя файла: {name}" ' \
             '{msg}'

    logging.basicConfig(level=logging.NOTSET,
                        format=FORMAT,
                        style="{",
                        filename=f"logs/{file_name.split('.')[0]}.log",
                        encoding="utf-8",
                        )

    try_exec("Rectangle(-2)", "Rectangle(5, -3)", """r = Rectangle(4, 4)
r.width = -3""", """r = Rectangle(4, 4)
r.height = -3""", """r = Rectangle(4, 4)
r.area()
r.perimeter()
r2 = Rectangle(4, 4)
r.width = 3
r.height = 3
r3 = r - r2
r4 = r + r2
""")
