"""
Напишите функцию, которая преобразует pickle файл
хранящий список словарей в табличный csv файл.
Для тестированию возьмите pickle версию файла из задачи
4 этого семинара.
Функция должна извлекать ключи словаря для заголовков
столбца из переданного файла.
"""
import csv
import pickle


def pickle_list_of_dirs_to_csv(pickle_file: str, csv_file: str):
    with (open(pickle_file, "rb") as pickle_f,
          open(csv_file, "w", newline="", encoding="utf-8") as csv_f):
        list_of_dirs = pickle.load(pickle_f)
        headers = list_of_dirs[0].keys()
        csv_write = csv.DictWriter(csv_f, fieldnames=headers,
                                   dialect='excel',
                                   quoting=csv.QUOTE_ALL)
        csv_write.writeheader()
        csv_write.writerows(list_of_dirs)


if __name__ == '__main__':
    PICKLE_FILE = "task_04.pickle"
    CSV_FILE = "task_06.csv"
    pickle_list_of_dirs_to_csv(PICKLE_FILE, CSV_FILE)
