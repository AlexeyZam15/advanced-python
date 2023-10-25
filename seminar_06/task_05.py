"""
� Добавьте в модуль с загадками функцию, которая хранит
словарь списков.
� Ключ словаря - загадка, значение - список с отгадками.
� Функция в цикле вызывает загадывающую функцию, чтобы
передать ей все свои загадки.
"""
from seminar_06.task_04 import guess_riddle


def pass_riddles(riddles: dict, attempts: int = 5):
    guessed = {}
    for k, v in riddles.items():
        guessed_attempt = guess_riddle(k, v, attempts)
        guessed[k] = guessed_attempt
    return guessed


if __name__ == '__main__':
    riddles = {"Не лает, не кусает,а в дом не пускает.": ["Замок", "Ворота", "Домофон", "Калитка", "Злой сосед"],
               "Зимой и летом одним цветом.": ["Ёлка", "Солнце", "Луна", "Земля"]}
    pass_riddles(riddles)
