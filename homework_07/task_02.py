"""Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.

Создайте файл __init__.py и запишите в него функцию rename_files"""

with open("__init__.py", mode="w", encoding="utf-8") as f:
    print("""from os import chdir, listdir, rename


def rename_files(desired_name: str, num_digits: int, source_ext: str, target_ext: str):
    chdir("test_folder")

    files = listdir()
    for i, file in enumerate(list(filter(lambda x: x.split(".")[-1] == source_ext, files))):
        rename(file, f"{desired_name}{str(i + 1).zfill(num_digits)}.{target_ext}")""", file=f)
