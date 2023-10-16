"""
✔ Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет
символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых
пользователем чисел до наибольшего включительно.
"""


def f(two_nums: str):
    list_ = [int(num) for num in two_nums.split(" ")[:2]]
    min_, max_ = min(list_), max(list_)
    return {chr(int(num)): int(num) for num in range(min_, max_ + 1)}


two_nums_ = input("Введите два числа через пробел")

print(f(two_nums_))
