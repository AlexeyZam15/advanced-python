"""
✔ Функция получает на вход список чисел и два индекса.
✔ Вернуть сумму чисел между между переданными индексами.
✔ Если индекс выходит за пределы списка, сумма считается
до конца и/или начала списка.
"""


def f(numbers: list[int | float], index1: int, index2: int):
    min_, max_ = min(index1, index2), max(index1, index2)

    if max_ > len(numbers):
        max_ = len(numbers)

    if min_ < 0:
        min_ = 0
    if max_ < 0:
        max_ = 0

    return sum(numbers[min_:max_ + 1])


numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

index1_ = 20

index2_ = -4

print(f(numbers1, index1_, index2_))
