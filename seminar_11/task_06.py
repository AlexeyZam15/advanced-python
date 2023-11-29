"""
Доработайте прошлую задачу.
Добавьте сравнение прямоугольников по площади
Должны работать все шесть операций сравнения
"""

from task_05 import Rectangle


class NewRectangle(Rectangle):
    def __init__(self, side: float):
        super().__init__(side, side)

    def __eq__(self, other):
        return self.area() == other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __ne__(self, other):
        return self.area() != other.area()


if __name__ == '__main__':
    rect1 = NewRectangle(3)
    rect2 = NewRectangle(3)
    print(f"Площадь 1-го прямоугольника = {rect1.area()}")
    print(f"Площадь 2-го прямоугольника = {rect2.area()}")
    print(f"Прямоугольники равны = {rect1 == rect2}")
    print(f"Прямоугольники неравны = {rect1 != rect2}")
    print(f"Прямоугольник 1 больше прямоугольника 2 = {rect1 > rect2}")
    print(f"Прямоугольник 1 больше или равен прямоугольнику 2 = {rect1 >= rect2}")
    print(f"Прямоугольник 1 меньше прямоугольника 2 = {rect1 < rect2}")
    print(f"Прямоугольник 1 меньше или равен прямоугольнику 2 = {rect1 <= rect2}")
