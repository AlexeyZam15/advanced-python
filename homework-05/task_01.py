"""
Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""
import os


def get_file_info(file_path: str):
    list_ = file_path.split("/")
    path = "/".join(list_[:-1]) + "/" if len(list_) > 1 else ""
    name = None
    extension = None
    name_extension = list_[-1].split(".")
    if len(name_extension) < 2:
        name = ""
        extension = f".{list_[-1]}"
    else:
        *name, extension = name_extension
        name = ".".join(name)
        extension = "." + extension
    return path, name, extension


def get_file_info_old(file_path: str):
    # найти последнее вхождение символа
    path_end = file_path.rfind("/")
    # вставить символ по индексу
    path = file_path[:path_end + 1]
    name_end = file_path.rfind(".")
    name = file_path[path_end + 1: name_end]
    extension = file_path[name_end:]
    return path, name, extension


# def get_file_info(file_path):
#     file_name = file_path.split("/")[-1]
#     file_extension = file_name.split(".")[-1]
#     path = file_path[:-len(file_name)]
#     return (path, file_name[:-len(file_extension)-1], "." + file_extension)


file_path = 'file_in_current_directory.txt'
file_info = get_file_info(file_path=file_path)
file_info2 = get_file_info_old(file_path=file_path)
print(file_info, file_info2, file_info == file_info2, sep="\n")
