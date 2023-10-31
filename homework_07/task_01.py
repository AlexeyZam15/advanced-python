"""
Напишите функцию группового переименования файлов в папке test_folder под названием rename_files. Она должна:

a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени.
Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
f. Папка test_folder доступна из текущей директории
"""
from os import path, mkdir, chdir, listdir, rename
from shutil import rmtree


def rename_files(desired_name: str, num_digits: int, source_ext: str, target_ext: str):
    chdir("test_folder")

    files = listdir()
    for i, file in enumerate(list(filter(lambda x: x.split(".")[-1] == source_ext, files))):
        rename(file, f"{desired_name}{str(i + 1).zfill(num_digits)}.{target_ext}")


if __name__ == '__main__':
    FOLDER = "test_folder"

    if path.exists(FOLDER):
        rmtree(FOLDER)

    mkdir(FOLDER)

    for i in range(1, 11):
        with open(f"{FOLDER}/{i}.txt", mode="w", encoding="utf-8"):
            pass

    with open(f"{FOLDER}/test.doc", mode="w", encoding="utf-8"):
        pass

    rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")

    print(*listdir())
