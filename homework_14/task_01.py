"""
Возьмите задачу Rectangle с прошлых семинаров. Напишите тесты для этой задачи.

Используйте модуль doctest.

Тесты:

test_width: Тестирование инициализации ширины. Созданы прямоугольники r1 с шириной 5 и r4 с отрицательной шириной (-2).
Убедимся, что r1.width корректно установлен на 5, а создание r4 вызывает исключение NegativeValueError.

test_height: Тестирование инициализации ширины и высоты. Созданы прямоугольники r2 с шириной 3 и высотой 4.
Проверяем, что r2.width равно 3 и r2.height равно 4.

test_perimeter: Тестирование вычисления периметра.
Создан прямоугольник r1 с шириной 5 и проверяем, что r1.perimeter() возвращает 20.
Также создан прямоугольник r2 с шириной 3 и высотой 4 и проверяем, что r2.perimeter() возвращает 14.

test_area: Тестирование вычисления площади. Создан прямоугольник r1 с шириной 5 и проверяем, что r1.area() возвращает 25.
Также создан прямоугольник r2 с шириной 3 и высотой 4 и проверяем, что r2.area() возвращает 12.

test_addition: Тестирование операции сложения. Созданы прямоугольники r1 с шириной 5 и r2 с шириной 3 и высотой 4.
Выполняем операцию сложения r1 + r2 и проверяем,
что полученный прямоугольник r3 имеет правильные значения ширины и высоты (8 и 6.0 соответственно).

test_subtraction: Тестирование операции вычитания. Созданы прямоугольники r1 с шириной 5 и r2 с шириной 3 и высотой 4.
Выполняем операцию вычитания r1 - r2 и проверяем,
что полученный прямоугольник r3 имеет правильные значения ширины и высоты (2 и 2.0 соответственно).

Запускать тесты не надо, автотест это сделает сам:


__file__ = None
doctest.testmod(extraglobs={'__file__': __file__})
"""
import doctest


class MyBaseException(Exception):
    pass


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
        self._width = float(width)
        if height is None:
            self._height = float(width)
        else:
            self.check_height(height)
            self._height = float(height)

    @staticmethod
    def check_width(width):
        if width < 0:
            raise NegativeValueError(f"Ширина должна быть положительной, а не {width}")

    @staticmethod
    def check_height(height):
        if height < 0:
            raise NegativeValueError(f"Высота должна быть положительной, а не {height}")

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
        return 2 * (self._width + self._height)

    def area(self):
        """
        Вычисляет площадь прямоугольника.

        Возвращает:
        - int: площадь прямоугольника
        """
        return self._width * self._height

    def __add__(self, other):
        """
        Определяет операцию сложения двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем сложения двух исходных прямоугольников

        test_addition: Тестирование операции сложения. Созданы прямоугольники r1 с шириной 5 и r2 с шириной 3 и высотой 4.
Выполняем операцию сложения r1 + r2 и проверяем,
что полученный прямоугольник r3 имеет правильные значения ширины и высоты (8 и 6.0 соответственно).
        >>> r1 = Rectangle(5)
        >>> r2 = Rectangle(3, 4)
        >>> r3 = r1 + r2
        >>> r3.width
        8.0
        >>> r3.height
        6.0
        """
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter // 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        """
        Определяет операцию вычитания одного прямоугольника из другого.

        Аргументы:
        - other (Rectangle): вычитаемый прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем вычитания вычитаемого прямоугольника из исходного

        test_subtraction: Тестирование операции вычитания. Созданы прямоугольники r1 с шириной 5 и r2 с шириной 3 и высотой 4.
Выполняем операцию вычитания r1 - r2 и проверяем,
что полученный прямоугольник r3 имеет правильные значения ширины и высоты (2 и 2.0 соответственно).
        >>> r1 = Rectangle(5)
        >>> r2 = Rectangle(3, 4)
        >>> r3 = r1 - r2
        >>> r3.width
        2.0
        >>> r3.height
        2.0
        """
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter // 2 - width
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


def test_width():
    """
    test_width: Тестирование инициализации ширины.
    Созданы прямоугольники r1 с шириной 5 и r4 с отрицательной шириной (-2).
    Убедимся, что r1.width корректно установлен на 5, а создание r4 вызывает исключение NegativeValueError.
    >>> r1 = Rectangle(5)
    >>> r1.width
    5.0
    >>> r4 = Rectangle(-2)
    Traceback (most recent call last):
    ...
    NegativeValueError: Ширина должна быть положительной, а не -2
    """


def test_height():
    """
    test_height: Тестирование инициализации ширины и высоты. Созданы прямоугольники r2 с шириной 3 и высотой 4.
    Проверяем, что r2.width равно 3 и r2.height равно 4.
    >>> r2 = Rectangle(3, 4)
    >>> r2.width
    3.0
    >>> r2.height
    4.0
    """


def test_perimeter():
    """
    test_perimeter: Тестирование вычисления периметра.
Создан прямоугольник r1 с шириной 5 и проверяем, что r1.perimeter() возвращает 20.
Также создан прямоугольник r2 с шириной 3 и высотой 4 и проверяем, что r2.perimeter() возвращает 14.
    >>> r1 = Rectangle(5)
    >>> r1.perimeter()
    20.0
    >>> r2 = Rectangle(3, 4)
    >>> r2.perimeter()
    14.0
    """


def test_area():
    """
    test_area: Тестирование вычисления площади. Создан прямоугольник r1 с шириной 5 и проверяем, что r1.area() возвращает 25.
Также создан прямоугольник r2 с шириной 3 и высотой 4 и проверяем, что r2.area() возвращает 12.
    >>> r1 = Rectangle(5)
    >>> r1.area()
    25.0
    >>> r2 = Rectangle(3, 4)
    >>> r2.area()
    12.0
    """


if __name__ == '__main__':
    import sys

    # Открываем файл для записи
    with open('pytest_output.txt', 'w') as file:
        # Перенаправляем stdout в файл
        sys.stdout = file

        # Запускаем pytest.main() с нужными параметрами
        __file__ = None

        doctest.testmod(extraglobs={'__file__': __file__})

    # Возвращаем stdout в исходное состояние
    sys.stdout = sys.__stdout__
    # Считываем содержимое файла
    with open('pytest_output.txt', 'r') as file:
        lines = file.readlines()
        # first_line = file.readline()
        # first_five_lines = lines[:1]

    import re

    file_name = "pytest_output.txt.txt"

    # Открываем файл на чтение
    with open('pytest_output.txt', "r") as file:
        # Считываем содержимое файла
        file_content = file.read()

    # Используем регулярное выражение для удаления "line" и чисел после него
    cleaned_content = re.sub(r'File "__main__", line \d+', '', file_content)

    # Записываем обновленное содержимое обратно в файл
    with open(file_name, "w") as file:
        file.write(cleaned_content)

    with open(file_name, 'r') as new_file:
        file_contents = new_file.read()
        # Выводим содержимое файла на экран
        print(file_contents)
