"""
Создайте класс-генератор.
Экземпляр класса должен генерировать факториал числа в
диапазоне от start до stop с шагом step.
Если переданы два параметра, считаем step=1.
Если передан один параметр, также считаем start=1.
"""
from math import factorial


class Factorial:
    def __init__(self, stop, start=1, step=1):
        self.stop = stop
        self.start = start
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.stop:
            self.start += self.step
            return factorial(self.start - self.step)
        raise StopIteration


if __name__ == '__main__':
    START = 1
    STOP = 10
    STEP = 1
    for fact in Factorial(STOP, START, STEP):
        print(fact)
