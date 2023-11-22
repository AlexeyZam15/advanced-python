"""
Создайте функцию generate_csv_file(file_name, rows), которая будет генерировать по три случайны числа в каждой строке,
 от 100-1000 строк, и записывать их в CSV-файл. Функция принимает два аргумента:
file_name (строка) - имя файла, в который будут записаны данные.
rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.

Создайте функцию find_roots(a, b, c), которая будет находить корни квадратного уравнения вида ax^2 + bx + c = 0.
Функция принимает три аргумента:
a, b, c (целые числа) - коэффициенты квадратного уравнения.

Функция возвращает:
None, если уравнение не имеет корней (дискриминант отрицателен).
Одно число, если уравнение имеет один корень (дискриминант равен нулю).
Два числа (корни), если уравнение имеет два корня (дискриминант положителен).

Создайте декоратор save_to_json(func), который будет оборачивать функцию find_roots. Декоратор выполняет следующие действия:
Читает данные из CSV-файла, переданного в аргументе функции, исходя из аргумента args[0].
Для каждой строки данных вычисляет корни квадратного уравнения с помощью функции find_roots.
Сохраняет результаты в формате JSON в файл results.json. Каждая запись JSON содержит параметры a, b, c и результаты вычислений.
Таким образом, после выполнения функций generate_csv_file и find_roots в файле results.json будет сохранена информация о параметрах и результатах вычислений для каждой строки данных из CSV-файла.

Пример

На входе:


generate_csv_file("input_data.csv", 101)
find_roots("input_data.csv")

with open("results.json", 'r') as f:
    data = json.load(f)

if 100<=len(data)<=1000:
    print(True)
else:
    print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

print(len(data)==101)
На выходе:


True
True
"""

import csv
from functools import wraps
from random import randint
from typing import Callable, Iterator
import json


def generate_csv_file(file_name: str, rows: int, min_number: int = 1, max_number: int = 10):
    with open(file_name, "w", encoding="utf-8", newline="") as f:
        csv_writer = csv.DictWriter(f, fieldnames=["a", "b", "c"], quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writeheader()
        data = []
        for _ in range(rows):
            row = {"a": randint(min_number, max_number), "b": randint(min_number, max_number),
                   "c": randint(min_number, max_number)}
            data.append(row)
        csv_writer.writerows(data)


def save_to_json(func: Callable):
    @wraps(func)
    def wrapper(*args):
        with open(args[0], "r", encoding="utf-8", newline="") as csv_file:
            csv_list_of_dicts: Iterator[dict] = csv.DictReader(csv_file, fieldnames=["a", "b", "c"])
            next(csv_list_of_dicts)
            json_data = []
            for row in csv_list_of_dicts:
                a, b, c = int(row["a"]), int(row["b"]), int(row["c"])
                json_dict = {"a": a, "b": b, "c": c, "roots": func(a, b, c)}
                json_data.append(json_dict)
            with open("results.json", "w", encoding="utf-8") as json_file:
                json.dump(json_data, json_file, ensure_ascii=False, indent=4)

    return wrapper


@save_to_json
def find_roots(a: int, b: int, c: int):
    if a == 0:
        return None
    d = b ** 2 - 4 * a * c
    if d < 0:
        return None
    elif d == 0:
        return -b / (2 * a)
    else:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)


if __name__ == '__main__':
    generate_csv_file("input_data.csv", 101)
    find_roots("input_data.csv")

    with open("results.json", 'r') as f:
        data = json.load(f)

    if 100 <= len(data) <= 1000:
        print(True)
    else:
        print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

    print(len(data) == 101)
