"""
✔ Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции.
"""
from random import randint, uniform


def random_numbers_file(filename: str, strings_count: int, min_=-1000, max_=1000):
    with open(filename, mode="a", encoding="utf-8") as f:
        for _ in range(strings_count):
            f.write(f"{randint(min_, max_)}|{uniform(min_, max_)}\n")


def read_file(filename: str):
    with open(filename, mode="r", encoding="utf-8") as f:
        return f.read()


if __name__ == '__main__':
    FILENAME = "task_01.txt"
    STRINGS_COUNT = 1

    random_numbers_file(FILENAME, STRINGS_COUNT)

    print(read_file(FILENAME))
