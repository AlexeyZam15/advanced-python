"""
� Создайте модуль с функцией внутри.
� Функция получает на вход загадку, список с возможными
вариантами отгадок и количество попыток на угадывание.
� Программа возвращает номер попытки, с которой была
отгадана загадка или ноль, если попытки исчерпаны.
"""


def guess_riddle(riddle: str, clues: list[str], attempts: int = 5):
    clues = [clue.lower() for clue in clues]
    print("_"*60)
    for attempt in range(0, attempts):
        print("Ответьте на загадку.", riddle)
        print(f"Осталось попыток: {attempts - attempt}")
        answer = input("Ваш ответ: ").lower()
        if answer in clues:
            print("Вы угадали, поздравляем!")
            return attempt + 1
        else:
            print("Неверно")
    print("Попытки кончились, попробуйте в следующий раз!")
    return 0


if __name__ == '__main__':
    RIDDLE = "Не лает, не кусает,а в дом не пускает."
    CLUES = ["Замок", "Ворота", "Домофон", "Калитка", "Злой сосед"]
    ATTEMPTS = 5
    guessed_attempt = guess_riddle(RIDDLE, CLUES, ATTEMPTS)
    print(f"Задача отгадана с попытки № {guessed_attempt}" if guessed_attempt else "Задача не отгадана")
