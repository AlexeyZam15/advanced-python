"""
✔ Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона.
"""

from task_02 import generate_name

from random import randint

from os import urandom, walk, mkdir, path

from shutil import rmtree


def create_random_file(extension: str, min_len_name: int = 6, max_len_name: int = 30, min_bytes: int = 256,
                       max_bytes: int = 4096, number_files: int = 42, folder: str = ""):
    if folder:
        if not path.exists(folder):
            mkdir(folder)
    for _ in range(number_files):
        random_name = generate_name(min_len_name, max_len_name)
        with open(f"{folder}/{random_name}.{extension}", mode="bw") as file:
            # случайно записанные байты
            file.write(urandom(randint(min_bytes, max_bytes)))


if __name__ == '__main__':
    EXTENSION = "txt"
    DIR = "task_04"

    if path.exists(DIR):
        rmtree(DIR)

    create_random_file(EXTENSION, folder=DIR)
    for dir_path, dir_name, file_name in walk(DIR):
        print("Files_number:", len(file_name))
        print("Files:", file_name)
