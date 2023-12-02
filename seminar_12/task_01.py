"""
Доработаем задачу 1.
Создайте менеджер контекста, который при выходе
сохраняет значения в JSON файл.
"""
from decimal import Decimal


class Factorial:
    def __init__(self, k, filename="factorial.json"):
        self.numbers = {}
        self.k = k
        self.filename = filename

    def __call__(self, number):
        self.number = number
        factorial = self.factorial(number)
        if number in self.numbers.keys():
            self.numbers.pop(number)
        self.numbers[number] = factorial
        if len(self.numbers) > self.k:
            self.numbers.pop(list(self.numbers.keys())[0])
        return factorial

    def factorial(self, number):
        if number in self.numbers.keys():
            return self.numbers[number]
        if number == 0:
            return 1
        return number * self.factorial(number - 1)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import json
        with open(self.filename, "w") as json_file:
            json.dump(self.numbers, json_file, ensure_ascii=False, indent=4)
        return True


if __name__ == '__main__':
    K = 3
    MAX_F = 10
    FILENAME = "task_02.json"
    with Factorial(K, FILENAME) as f:
        for i in range(MAX_F + 1):
            f(i)
    # print(", ".join([f"f({i}) = {f(i)}" for i in range(MAX_F)]))
    print(f"Last {K} factorial numbers: ", ",\n".join([f"f({k}) = {v}" for k, v in f.numbers.items()]))
