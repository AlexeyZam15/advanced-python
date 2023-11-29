"""
Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания
(time.time)
"""
import time


class MyString(str):
    """Класс MyString, наследующийся класса str"""
    def __new__(cls, author, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        return instance

    def __init__(self, author, *args, **kwargs):
        """
        Инициализация класса MyString.
        Хранит имя автора и время создания строки.
        Дополнительно хранит аргументы для str.
        :param author: имя автора
        :param time: время создания строки (time.time)
        :param args: аргументы для str, первый аргумент - text
        :param kwargs: аргументы для str
        """
        self.author = author
        self.time = time.time()


if __name__ == '__main__':
    s = MyString("Спенглер", 'Hello World', )
    print(s)
    print(s.author)
    print(s.time)
    print(s.upper())
    print(s.lower())
    print(s.swapcase() * 4)
