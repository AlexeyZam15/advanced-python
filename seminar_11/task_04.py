"""
Доработаем класс Архив из задачи 2.
Добавьте методы представления экземпляра для программиста
и для пользователя.
"""

from task_02 import Archive


class NewArchive(Archive):
    """Класс архив, для хранения чисел и строк"""

    def __init__(self, number: int, string: str):
        super().__init__(number, string)

    def __repr__(self):
        """Метод для представления экземпляра для программиста"""
        return f"NewArchive({self.number}, {self.string})"

    def __str__(self):
        """Метод для представления экземпляра для пользователя"""
        return f"Число: {self.number}, строка: {self.string}"


if __name__ == '__main__':
    a = NewArchive(1, 'a')
    print(f"{a.__str__() = }")
    print(f"{a.__repr__() = }")
