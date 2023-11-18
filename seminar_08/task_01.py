"""
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее
файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
"""
import json


def json_format(txt_file: str, new_file: str):
    file_list = list()
    file_dict = {"pairs": file_list}

    with open(txt_file, "r", encoding="utf-8") as f:
        for row in f.read().split("\n")[:-1]:
            row_split = row.split("|")
            file_list.append({"name": row_split[0].title(),
                              "product": row_split[1] if not row_split[1].isdigit() else float(row_split[1])})

    new_file += ".json"

    with open(new_file, "w", encoding="utf-8") as f:
        json.dump(file_dict, f, ensure_ascii=False, indent=4)

    return new_file


if __name__ == '__main__':
    FILE = "../seminar_07/task_03.txt"

    NEW_FILE_NAME = "task_01"

    new_file_ = json_format(FILE, NEW_FILE_NAME)

    with open(new_file_, "r", encoding="utf-8") as f:
        print(f.read())
