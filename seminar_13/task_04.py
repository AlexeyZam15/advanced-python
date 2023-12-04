"""
Вспоминаем задачу из семинара 8 про сериализацию данных,
где в бесконечном цикле запрашивали имя, личный
идентификатор и уровень доступа (от 1 до 7) сохраняя
информацию в JSON файл.
Напишите класс пользователя, который хранит эти данные в
свойствах экземпляра.
Отдельно напишите функцию, которая считывает информацию
из JSON файла и формирует множество пользователей.
"""
import json


class User:
    def __init__(self, access_level, user_id, name):
        self.access_level = access_level
        self.user_id = user_id
        self.name = name

    def __str__(self):
        return f"User {self.user_id} ({self.name}) has access level {self.access_level}"


def read_users(json_file):
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    created_users = []
    for access_level, users in data.items():
        for user_id, name in users.items():
            created_users.append(User(access_level, user_id, name))
    return created_users


if __name__ == '__main__':
    JSON_FILE = "task_04.json"
    users = read_users(JSON_FILE)
    print(*users, sep="\n")
