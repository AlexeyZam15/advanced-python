"""
Напишите декоратор, который сохраняет в json файл
параметры декорируемой функции и результат, который она
возвращает. При повторном вызове файл должен
расширяться, а не перезаписываться.
Каждый ключевой параметр сохраните как отдельный ключ
json словаря.
Для декорирования напишите функцию, которая может
принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой
функции.
"""
import json
from functools import wraps
from os import path
from typing import Callable


def save_to_json(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        json_file = []
        if path.exists(wrapper.__name__ + ".json"):
            with open(wrapper.__name__ + ".json", "r", encoding="utf-8") as f:
                json_file = json.load(f)

        with open(wrapper.__name__ + ".json", "w", encoding="utf-8") as f:
            file_dict = {"args": args, "kwargs": {key: value for key, value in kwargs.items()}, "result": result}
            json_file.append(file_dict)
            json.dump(json_file, f, ensure_ascii=False, indent=4)
        return result

    return wrapper


@save_to_json
def compose_line(*args, **kwargs):
    return ", ".join([str(arg) for arg in args] + [f"{key}={value}" for key, value in kwargs.items()])


if __name__ == '__main__':
    compose_line(1, 2, 3, 4, 5, one=1, two=2, three=3, four=4, five=5)
    compose_line(6, 7, 8, 9, 10, six=6, seven=7, eight=8, nine=9, ten=10)
    compose_line(11, 12, 13, 14, 15, eleven=11, twelve=12, thirteen=13, fourteen=14, fifteen=15)
