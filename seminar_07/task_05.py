"""
✔ Доработаем предыдущую задачу.
✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
✔ Расширения и количество файлов функция принимает в качестве параметров.
✔ Количество переданных расширений может быть любым.
✔ Количество файлов для каждого расширения различно.
✔ Внутри используйте вызов функции из прошлой задачи
"""

from os import path, mkdir, chdir

from shutil import rmtree


def new_create_random_files(extensions_files_number: dict[str: int], folder=""):
    if folder:
        if not path.exists(folder):
            mkdir(folder)
        chdir(folder)

    from task_04 import create_random_file
    for extension, files_number in extensions_files_number.items():
        create_random_file(extension, number_files=files_number, folder=extension)


if __name__ == '__main__':
    EXTENSIONS_FILES_NUMBER = {"txt": 4,
                               "bat": 5,
                               "md": 3}

    FOLDER = "task_05"

    for DIR in EXTENSIONS_FILES_NUMBER:
        if path.exists(DIR):
            rmtree(DIR)

    new_create_random_files(EXTENSIONS_FILES_NUMBER, folder=FOLDER)
