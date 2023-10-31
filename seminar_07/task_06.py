"""
✔ Дорабатываем функции из предыдущих задач.
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
"""

from task_02 import generate_name

from random import randint

from os import urandom, mkdir, path, chdir


def create_random_file(extension: str, min_len_name: int = 6, max_len_name: int = 30, min_bytes: int = 256,
                       max_bytes: int = 4096, number_files: int = 42, folder: str = ""):
    if folder:
        if not path.exists(folder):
            mkdir(folder)

    created_files = []

    for _ in range(number_files):
        random_name = generate_name(min_len_name, max_len_name)
        if path.exists(f"{folder}/{random_name}.{extension}"):
            continue
        if folder:
            file_name = f"{folder}/{random_name}.{extension}"
        else:
            file_name = f"{random_name}.{extension}"
        created_files.append(file_name)
        with open(file_name, mode="bw") as file:
            # случайно записанные байты
            file.write(urandom(randint(min_bytes, max_bytes)))

    return created_files


def new_create_random_files(extensions_files_number: dict[str: int], folder=""):
    if folder:
        if not path.exists(folder):
            mkdir(folder)
        chdir(folder)

    created_files = []
    for extension, files_number in extensions_files_number.items():
        created_files.extend(create_random_file(extension, number_files=files_number, folder=extension))
    return created_files


if __name__ == '__main__':
    EXTENSIONS_FILES_NUMBER = {"txt": 4,
                               "bat": 5,
                               "md": 3}

    FOLDER = "task_06"

    print(new_create_random_files(EXTENSIONS_FILES_NUMBER, FOLDER))
