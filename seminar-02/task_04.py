"""
✔ Напишите программу, которая вычисляет площадь
круга и длину окружности по введённому диаметру.
✔ Диаметр не превышает 1000 у.е.
✔ Точность вычислений должна составлять
не менее 42 знаков после запятой.
"""

import math


def area_area_and_length(diameter: float):
    if diameter > 1000:
        raise ValueError("Диаметр не может превышать 1000 у.е.")
    radius = diameter / 2
    area = math.pi * radius ** 2
    length = 2 * math.pi * radius
    return area, length


diameter_1 = float(input("Введите диаметр окружности: "))

area_1, length_1 = area_area_and_length(diameter_1)

print(f"Площадь круга: {area_1:.42f}")
print(f"Длина окружности: {length_1:.42f}")
