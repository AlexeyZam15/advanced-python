"""
Ваша задача - написать программу, которая принимает на вход директорию и рекурсивно обходит эту директорию и все вложенные директории.
Результаты обхода должны быть сохранены в нескольких форматах: JSON, CSV и Pickle. Каждый результат должен содержать следующую информацию:

Путь к файлу или директории: Абсолютный путь к файлу или директории. Тип объекта: Это файл или директория.
Размер: Для файлов - размер в байтах, для директорий - размер, учитывая все вложенные файлы и директории в байтах. Важные детали:

Для дочерних объектов (как файлов, так и директорий) укажите родительскую директорию.

Для файлов сохраните их размер в байтах.

Для директорий, помимо их размера, учтите размер всех файлов и директорий, находящихся внутри данной директории, и вложенных директорий.

Программа должна использовать рекурсивный обход директорий, чтобы учесть все вложенные объекты.

Результаты должны быть сохранены в трех форматах: JSON, CSV и Pickle. Форматы файлов должны быть выбираемыми.

Для обхода файловой системы вы можете использовать модуль os.

Вам необходимо написать функцию traverse_directory(directory), которая будет выполнять обход директории и возвращать результаты в виде списка словарей.
После этого результаты должны быть сохранены в трех различных файлах (JSON, CSV и Pickle) с помощью функций save_results_to_json, save_results_to_csv и save_results_to_pickle.
"""
import csv
import json
import os
import pickle


def get_dir_size(path: str):
    size = 0
    for root, dirs, files in os.walk(path):
        for directory in dirs:
            size += get_dir_size(os.path.join(root, directory))
        for file in files:
            size += os.path.getsize(os.path.join(root, file))
    return size


def traverse_directory(path: str):
    # # проверка на абсолютный путь
    # if not os.path.isabs(path):
    #     # получить абсолютный путь до указанной папки
    #     path = os.path.abspath(path)
    res_list = []
    # обход папок
    for root, dirs, files in os.walk(path):
        for file in files:
            temp_dict = dict()
            # путь до файла
            temp_dict["Path"] = os.path.join(root, file)
            # тип объекта
            temp_dict["Type"] = "File"
            # # родительская директория
            # temp_dict["parent"] = os.path.split(root)[-1]

            # размер файла
            temp_dict["Size"] = os.path.getsize(temp_dict["Path"])
            res_list.append(temp_dict)

        for directory in dirs:
            temp_dict = dict()
            # путь до директории
            temp_dict["Path"] = os.path.join(root, directory)
            # тип объекта
            temp_dict["Type"] = "Directory"
            # # родительская директория
            # temp_dict["parent"] = os.path.split(root)[-1]

            # размер папки вместе со всеми вложенными папками и файлами
            temp_dict["Size"] = get_dir_size(temp_dict["Path"])
            res_list.append(temp_dict)

    return res_list


def save_results_to_json(list_of_dirs: list, file: str = "JSON.json"):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(list_of_dirs, f, ensure_ascii=False, indent=4)


def save_results_to_csv(list_of_dirs: list, file: str = "CSV.csv"):
    with open(file, "w", encoding="utf-8", newline="") as f:
        headers = list_of_dirs[0].keys()
        csv_writer = csv.DictWriter(f, fieldnames=headers)
        csv_writer.writeheader()
        csv_writer.writerows(list_of_dirs)


def save_results_to_pickle(list_of_dirs: list, file: str = "PICKLE.pickle"):
    with open(file, "wb") as f:
        pickle.dump(list_of_dirs, f)


if __name__ == '__main__':
    DIRECTORY = ".."
    list_of_dirs_ = traverse_directory(DIRECTORY)
    print(*list_of_dirs_, sep="\n")
    save_results_to_json(list_of_dirs_)
    save_results_to_csv(list_of_dirs_)
    save_results_to_pickle(list_of_dirs_)
