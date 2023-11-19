"""
Напишите функцию, которая ищет json файлы в указанной
директории и сохраняет их содержимое в виде
одноимённых pickle файлов.
"""
import os

import json

import pickle


def json_to_pickle(directory: str):
    start_path = os.getcwd()
    os.chdir(directory)
    for file in os.listdir(os.getcwd()):
        if file.endswith(".json"):
            with (open(file, "r", encoding="utf-8") as json_file,
                  open(file.replace(".json", ".pickle"), 'wb') as pickle_file):
                json_object = json.load(json_file)
                pickle.dump(json_object, pickle_file)
    os.chdir(start_path)


def read_pickle_files(directory: str):
    start_path = os.getcwd()
    os.chdir(directory)
    for file in os.listdir(os.getcwd()):
        if file.endswith(".pickle"):
            with open(file, "rb") as f:
                print(pickle.load(f))
    os.chdir(start_path)


if __name__ == '__main__':
    DIRECTORY = "."
    json_to_pickle(DIRECTORY)
    read_pickle_files(DIRECTORY)
