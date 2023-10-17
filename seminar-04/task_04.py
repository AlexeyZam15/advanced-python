"""
✔ Функция получает на вход список чисел.
✔ Отсортируйте его элементы in place без использования
встроенных в язык сортировок.
✔ Как вариант напишите сортировку пузырьком.
Её описание есть в википедии.
"""
import random


def bubble_sort(numbers: list[int]):
    for count in range(len(numbers)):
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
    return numbers


MAX_RANDOM = 20

MIN_RANDOM = 0

NUMBERS_COUNT = 10

numbers_ = [random.randint(MIN_RANDOM, MAX_RANDOM) for _ in range(NUMBERS_COUNT)]

print("Изначальный список чисел: ", numbers_)

print("Отсортированный список", bubble_sort(numbers_))
