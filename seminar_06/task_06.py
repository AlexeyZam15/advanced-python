"""
� Добавьте в модуль с загадками функцию, которая
принимает на вход строку (текст загадки) и число (номер
попытки, с которой она угадана).
� Функция формирует словарь с информацией о результатах
отгадывания.
� Для хранения используйте защищённый словарь уровня
модуля.
� Отдельно напишите функцию, которая выводит результаты
угадывания из защищённого словаря в удобном для чтения
виде.
� Для формирования результатов используйте генераторное
выражение.
"""

from seminar_06.task_05 import pass_riddles

_guessed_numbers = {}


def solved_riddles(guessed_riddles: dict):
    for k, v in guessed_riddles.items():
        _solved_riddles(k, v)


def _solved_riddles(riddle: str, guessed_attempt: int):
    _guessed_numbers[riddle] = guessed_attempt


def text_guessed_results():
    yield "_" * 60 + "\n"
    for k, v in _guessed_numbers.items():
        yield f'Загадка: {k}\nОтгадана с попытки: {v}\n' if v else f'Загадка: {k}\nНе отгадана\n'


if __name__ == '__main__':
    riddles = {"Не лает, не кусает,а в дом не пускает.": ["Замок", "Ворота", "Домофон", "Калитка", "Злой сосед"],
               "Зимой и летом одним цветом.": ["Ёлка", "Солнце", "Луна", "Земля"]}
    solved_riddles(pass_riddles(riddles))
    print(*text_guessed_results())
