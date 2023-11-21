"""
Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функцию угадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами
из диапазонов.
"""
from random import randint
from typing import Callable


def guess_game(func: Callable):
    number = int(input("Загадайте число от 1 до 100: "))
    attempts = int(input("Введите кол-во попыток для отгадывания от 1 до 10: "))

    def wrapper():
        nonlocal number
        nonlocal attempts
        if number not in range(1, 101):
            number = randint(1, 100)
        if attempts not in range(1, 11):
            attempts = randint(1, 10)
        return func(number, attempts)

    return wrapper


@guess_game
def guess_number(number: int, attempts: int):
    for attempt in range(attempts, 0, -1):
        # print(number,attempts)
        print(f"Попробуйте отгадать число, осталось попыток: {attempt}")
        input_num = int(input("Введите число: "))
        if input_num == number:
            print("Число угадано")
            return
        print("Неверно")
    print("Попытки кончились, число не угадано")
    return


guess = guess_number()
