"""
Объедините функции из прошлых задач.
Функцию угадайку задекорируйте:
○ декораторами для сохранения параметров,
○ декоратором контроля значений и
○ декоратором для многократного запуска.
Выберите верный порядок декораторов.
"""
import json
from functools import wraps
from os import path
from random import randint
from typing import Callable


def run_times(times: int):
    def run_func(func: Callable):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
            return

        return wrapper

    return run_func


def guess_game(func: Callable):
    @wraps(func)
    def wrapper():
        number = int(input("Загадайте число от 1 до 100: "))
        attempts = int(input("Введите кол-во попыток для отгадывания от 1 до 10: "))

        if number not in range(1, 101):
            number = randint(1, 100)
        if attempts not in range(1, 11):
            attempts = randint(1, 10)
        return func(number, attempts)

    return wrapper


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


@run_times(3)
@guess_game
@save_to_json
def guess_number(number: int, attempts: int):
    for attempt in range(attempts, 0, -1):
        # print(number,attempts)
        print(f"Попробуйте отгадать число, осталось попыток: {attempt}")
        input_num = int(input("Введите число: "))
        if input_num == number:
            print("Число угадано")
            return f"Число угадано c попытки № {attempts - attempt + 1}"
        print("Неверно")
    print("Попытки кончились, число не угадано")
    return "Попытки кончились, число не угадано"


if __name__ == '__main__':
    guess_number()
