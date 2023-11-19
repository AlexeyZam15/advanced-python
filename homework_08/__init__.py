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
