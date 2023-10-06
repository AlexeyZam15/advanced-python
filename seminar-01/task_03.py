"""
Задание №6.
Напишите программу, которая запрашивает год и проверяет его на високосность.
Распишите все возможные проверки в цепочке elif.
Откажитесь от магических чисел
Обязательно учтите год ввода Григорианского календаря
В коде должны быть один input и один print
"""


def check_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False


def check_leap_year_2(year):
    return True if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else False


def print_leap_year(year, mode=True):
    if mode:
        leap_year = check_leap_year_2(year)
    else:
        leap_year = check_leap_year(year)
    text = ""
    if leap_year:
        text = (f"Год {year} високосный")
    else:
        text = (f"Год {year} не високосный")
    print(text)


year = int(input("Введите год: "))
print_leap_year(year)
print_leap_year(year, False)
