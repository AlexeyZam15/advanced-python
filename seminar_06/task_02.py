"""
� Создайте модуль с функцией внутри.
� Функция принимает на вход три целых числа: нижнюю и
верхнюю границу и количество попыток.
� Внутри генерируется случайное число в указанных границах
и пользователь должен угадать его за заданное число
попыток.
� Функция выводит подсказки “больше” и “меньше”.
� Если число угадано, возвращается истина, а если попытки
исчерпаны - ложь.
"""


def _input_number(text: str):
    try:
        answer = int(input(text))
    except Exception:
        answer = ""
    return answer


def guess_number(lower_limit: int = 0, upper_limit: int = 10, attempts: int = 5):
    """
    A random number is generated within the specified range,
    and you need to guess it by entering it in a certain number of attempts
    :param lower_limit: lower limit in range of random number
    :param upper_limit: upper limit in range of random number
    :param attempts: Number of attempts for which you need to guess the number
    :return: If the number is guessed, the truth is returned, and if the attempts are exhausted, it is false
    """
    from random import randint

    random_number = randint(lower_limit, upper_limit)
    input_text = f"Угадайте число от {lower_limit} до {upper_limit}: "
    answer = _input_number(input_text)
    attempts -= 1
    while answer != random_number and attempts > 0:
        print(f"Не угадали! Осталось попыток: {attempts}")
        if isinstance(answer, int):
            print("Больше" if random_number > answer else "Меньше")
        attempts -= 1
        answer = _input_number(input_text)
    if attempts + 1:
        print("Угадали, поздравляем!")
        return True
    print("Не угадали, попытки кончились")
    return False


if __name__ == '__main__':
    LOWER_LIMIT = 0
    UPPER_LIMIT = 5
    ATTEMPTS = 5
    guess_number(LOWER_LIMIT, UPPER_LIMIT, ATTEMPTS)
