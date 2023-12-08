"""
На семинарах по ООП был создан класс прямоугольник
хранящий длину и ширину, а также вычисляющую периметр,
площадь и позволяющий складывать и вычитать
прямоугольники беря за основу периметр.
Напишите 3-7 тестов unittest для данного класса.
"""
from unittest import TestCase, main

from homework_13.task_01 import Rectangle, NegativeValueError


class RectangleTest(TestCase):

    def test_creation(self):
        r1 = Rectangle(2, 3)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.perimeter(), 10)
        self.assertEqual(r1.area(), 6)

    def test_str_repr(self):
        r1 = Rectangle(2, 3)
        self.assertEqual(str(r1), 'Прямоугольник со сторонами 2 и 3')
        self.assertEqual(repr(r1), 'Rectangle(2, 3)')

    def test_set_params(self):
        r1 = Rectangle(2, 3)
        r1.width = 4
        self.assertEqual(r1.width, 4)
        r1.height = 4
        self.assertEqual(r1.height, 4)

    def test_add(self):
        r1 = Rectangle(2, 3)
        r2 = Rectangle(3, 4)
        r3 = r1 + r2
        self.assertEqual(r3.perimeter(), 24)
        self.assertEqual(r3.area(), 35)

    def test_sub(self):
        r1 = Rectangle(2, 3)
        r2 = Rectangle(3, 4)
        r3 = r1 - r2
        self.assertEqual(r3.perimeter(), 4)
        self.assertEqual(r3.area(), 1)

    def test_lt(self):
        r1 = Rectangle(2, 3)
        r2 = Rectangle(3, 4)
        self.assertTrue(r1 < r2)

    def test_eq(self):
        r1 = Rectangle(2, 3)
        r2 = Rectangle(2, 3)
        self.assertTrue(r1 == r2)

    def test_le(self):
        r1 = Rectangle(2, 3)
        r2 = Rectangle(3, 4)
        self.assertTrue(r1 <= r2)

    def test_creation_invalid_width(self):
        with self.assertRaises(NegativeValueError):
            Rectangle(-1, 2)

    def test_creation_invalid_height(self):
        with self.assertRaises(NegativeValueError):
            Rectangle(0, -2)

    def test_set_invalid_width(self):
        r1 = Rectangle(2, 3)
        with self.assertRaises(NegativeValueError):
            r1.width = -1

    def test_set_invalid_height(self):
        r1 = Rectangle(2, 3)
        with self.assertRaises(NegativeValueError):
            r1.height = -1


if __name__ == '__main__':
    main(verbosity=2)
