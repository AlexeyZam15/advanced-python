"""
Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Распечатайте его как pickle строку
"""
import csv

import pickle


def print_csv_as_pickle_string(csv_file: str):
    with open(csv_file, "r", encoding="utf-8") as f:
        lines = list(csv.reader(f))
        pickle_data = pickle.dumps(lines)
        print(pickle_data)
    return pickle_data


if __name__ == '__main__':
    CSV_FILE = "task_06.csv"
    print(pickle.loads(print_csv_as_pickle_string(CSV_FILE)))
