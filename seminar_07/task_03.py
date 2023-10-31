"""
✔ Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
✔ если результат умножения отрицательный, сохраните имя
записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя
прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк,
сколько в более длинном файле.
✔ При достижении конца более короткого файла,
возвращайтесь в его начало.
"""
from math import prod
from task_01 import read_file


def get_cycle_list_value(index: int, list_: list):
    if index < len(list_):
        return list_[index]
    else:
        return list_[index - len(list_)]


def mult_pairs_of_numbers(file_name_with_numbers: str, filename_with_names: str, new_filename: str):
    with open(file_name_with_numbers, mode="r", encoding="utf-8") as numbers_file:
        mult_list = [prod([float(j) for j in i.split("|")]) for i in numbers_file.read().split("\n")[:-1]]

    with open(filename_with_names, mode="r", encoding="utf-8") as names_file:
        names_list = names_file.read().split("\n")[:-1]

    with open(new_filename, mode="w", encoding="utf-8") as result_file:
        i = 0
        while i < max(len(mult_list), len(names_list)):
            number = get_cycle_list_value(i, mult_list)
            name = get_cycle_list_value(i, names_list)
            if number < 0:
                result_file.write(f"{name.lower()}|{abs(number)}")
            else:
                result_file.write(f"{name.upper()}|{int(number)}")
            result_file.write("\n")
            i += 1


if __name__ == '__main__':
    FILENAME_WITH_NUMBERS = "task_01.txt"
    FILENAME_WITH_NAMES = "task_02.txt"
    NEW_FILENAME = "task_03.txt"

    mult_pairs_of_numbers(FILENAME_WITH_NUMBERS, FILENAME_WITH_NAMES, NEW_FILENAME)
    print(read_file(NEW_FILENAME))
