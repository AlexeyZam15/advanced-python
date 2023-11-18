"""
Напишите функцию, которая в бесконечном цикле
запрашивает имя, личный идентификатор и уровень
доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в
JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо
от уровня доступа.
При перезапуске функции уже записанные в файл данные
должны сохраняться.
"""
import json

import os


def infinite_query(file: str):
    min_access_level = 1
    max_access_level = 7
    access_levels = [i for i in range(min_access_level, max_access_level + 1)]
    personal_ids = list()
    """проверка на существование файла"""
    if os.path.exists(file):
        with open(file, "r", encoding="utf-8") as f:
            json_dict = json.load(f)
        access_levels_dict = json_dict["access levels"]
        for personal_ids_ in access_levels_dict.values():
            for personal_id in personal_ids_:
                personal_ids.append(personal_id)
        print(personal_ids)
    else:
        access_levels_dict = {str(i): dict() for i in access_levels}
        json_dict = {"access levels": access_levels_dict}
        with open(file, "w", encoding="utf-8") as f:
            json.dump(json_dict, f, ensure_ascii=False, indent=4)

    while True:
        name = input(f"Введите имя: ")

        personal_id = input(f"Введите уникальный личный идентификатор: ")
        while personal_id in personal_ids:
            print("Введён повторяющийся идентификатор")
            personal_id = input(f"Введите уникальный личный идентификатор: ")
        personal_ids.append(personal_id)

        access_level = input(f"Введите уровень доступа от {min_access_level} до {max_access_level}: ")
        while access_level.isdigit() and int(access_level) not in access_levels:
            print(f"Уровень доступа должен быть цифрой от {min_access_level} до {max_access_level}")
            access_level = input(f"Введите уровень доступа от {min_access_level} до {max_access_level}: ")

        access_levels_dict[access_level][personal_id] = name
        with open(file, "w", encoding="utf-8") as f:
            json.dump(json_dict, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    FILE_NAME = "task_02.json"
    infinite_query(FILE_NAME)
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        print(f.read())
