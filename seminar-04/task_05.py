"""
✔ Функция принимает на вход три списка одинаковой длины:
✔ имена str,
✔ ставка int,
✔ премия str с указанием процентов вида «10.25%».
✔ Вернуть словарь с именем в качестве ключа и суммой
премии в качестве значения.
✔ Сумма рассчитывается как ставка умноженная на процент премии.
"""


def get_awards(names: list[str], salaries: list[int], awards: list[str]):
    earn = {}
    for name, salary, award in zip(names, salaries, awards):
        earn[name] = salary * (float(award.replace("%", "")) / 100)
    return earn


names1 = ["Иван", "Николай", "Пётр"]
salaries1 = [125_000, 96_000, 109_000]
awards1 = ["10%", "25%", "13%", "99%"]

print(get_awards(names1, salaries1, awards1))
