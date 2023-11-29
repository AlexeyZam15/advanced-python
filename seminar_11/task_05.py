"""
Дорабатываем класс прямоугольник из прошлого семинара.
Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр прямоугольника.
Складываем и вычитаем периметры, а не длину и ширину.
При вычитании не допускайте отрицательных значений.
"""


class Rectangle:
    """
    Класс прямоугольник
    """

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

    def perimeter(self):
        """
        Расчёт периметра прямоугольника по сторонам
        :return: периметр прямоугольника
        """
        return 2 * (self.length + self.width)

    def area(self):
        """
        Расчёт площади прямоугольника по сторонам
        :return: площадь прямоугольника
        """
        return self.length * self.width

    def __add__(self, other):
        new_perimeter = self.perimeter() + other.perimeter()
        return Rectangle(new_perimeter / 2)

    def __sub__(self, other):
        if other.perimeter() <= self.perimeter():
            return None
        new_perimeter = self.perimeter() - other.perimeter()
        return Rectangle(new_perimeter / 2)

    def __str__(self):
        if self.width != self.length:
            return f"Прямоугольник со сторонами {self.length} и {self.width}"
        return f"Квадрат со стороной {self.length}"


if __name__ == '__main__':
    rect1 = Rectangle(3, 4)
    rect2 = Rectangle(3, 4)
    print(f"Периметр 1-го прямоугольника = {rect1.perimeter()}")
    print(f"Периметр 2-го прямоугольника = {rect2.perimeter()}")
    res1 = rect1 + rect2
    print(f"Прямоугольник, составленный при сложении 1-го и 2-го прямоугольников = {res1}")
    res2 = rect1 - rect2
    print(f"Прямоугольник, составленный при вычитании 1-го и 2-го прямоугольников = {res2}")
