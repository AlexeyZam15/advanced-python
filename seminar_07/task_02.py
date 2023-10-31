"""
✔ Напишите функцию, которая генерирует
псевдоимена.
✔ Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.
"""
from random import randint, choice
from task_01 import read_file


def generate_name(min_len: int = 4, max_len: int = 7):
    # гласные буквы русского алфавита
    vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
    # согласные буквы русского алфавита
    consonants = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш',
                  'щ']
    name = ""
    for i in range(randint(min_len, max_len)):
        if i % 2 == 0:
            name += choice(vowels)
        else:
            name += choice(consonants)
    return name


def pseudo_names_file(filename: str, names_count: int):
    with open(filename, mode="w", encoding="utf-8") as f:
        for _ in range(names_count):
            f.write(f"{generate_name()}\n")

    if __name__ == '__main__':
        FILENAME = "task_02.txt"
        NAMES_COUNT = 5

        pseudo_names_file(FILENAME, NAMES_COUNT)
        print(read_file(FILENAME))
