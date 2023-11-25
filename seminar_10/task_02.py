"""
Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании
экземпляра.
У класса должно быть два метода, возвращающие периметр
и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат
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


if __name__ == '__main__':
    rect = Rectangle(3, 4)
    print(f"Длина прямоугольника = {rect.length}", f"Ширина прямоугольника = {rect.width}", sep="\n")
    print(f"Периметр прямоугольника = {rect.perimeter()}")
    print(f"Площадь прямоугольника = {rect.area()}")
    print("_" * 60)
    rect = Rectangle(3)
    print(f"Стороны квадрата = {rect.length}")
    print(f"Периметр квадрата = {rect.perimeter()}")
    print(f"Площадь квадрата = {rect.area()}")
