"""
Вы работаете над разработкой программы для проверки корректности даты, введенной пользователем.
На вход будет подаваться дата в формате "день.месяц.год".
Ваша задача - создать программу, которая проверяет, является ли введенная дата корректной или нет.

Ваша программа должна предоставить ответ "True" (дата корректна) или "False" (дата некорректна) в зависимости от результата проверки.
"""

_DAYS_IN_MONTH = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31,
                  11: 30, 12: 31}


def _checking_leap_year(year: int):
    """
    Проверка года на високосность
    :param year: число года
    :return: True, если год - високосный, иначе False
    """
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False


def _check_date(date: str):
    """
    Checking the date for correctness
    :param date: date in the format DD.MM.YYYY
    :return: returns True if the date can exist or a False if such a date is not possible
    """
    try:
        day, month, year = date.split(".")[:3]
    except ValueError:
        raise ValueError("Строка не соответствует формату DD.MM.YYYY")
    # преобразование в число
    try:
        day = int(day)
        month = int(month)
        year = int(year)
    except ValueError:
        raise ValueError("Дата должны состоять из чисел")
    # проверка на правильные числа месяца, года, и дня
    if month < 1 or month > 12:
        raise ValueError("Неверное число месяца, число месяца должно быть не меньше 1, и не больше 12")
    if year < 1 or year > 9999:
        raise ValueError("Неверный год, год должен быть не меньше 1, и не больше 9999")
    day_limit = _DAYS_IN_MONTH[month]
    if month == 2 and _checking_leap_year(year):  # проверка на високосный год, если месяц - февраль
        day_limit = 29
    if day < 1 or day > day_limit:
        raise ValueError(f"Неверное число дня, число дня этого месяца должно быть не меньше 1, и не больше {day_limit}")


def check_date(date: str):
    try:
        _check_date(date)
    except ValueError as ve:
        return False
    return True


date_to_prove = "31.6.2022"

print(check_date(date_to_prove))
