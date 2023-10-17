"""
✔ Функция получает на вход словарь с названием компании в качестве ключа
и списком с доходами и расходами (3-10 чисел) в качестве значения.
✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
"""


def check_profit(company_finances: dict[str:list[int | float]]):
    if all(map(lambda x: x >= 0, [sum(i) for i in company_finances.values()])):
        return True
    return False


company_finances_1 = {
    "Inova": [1, 1, -2, 1],
    "Hyundai": [-2, -2, -2, 0]
}

company_finances_2 = {
    "Inova": [1, 1, 2, 1],
    "Hyundai": [2, 2, 2, 0]
}

print(check_profit(company_finances_1))

print(check_profit(company_finances_2))
