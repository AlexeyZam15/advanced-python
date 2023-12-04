"""
Допишите в вашу задачу Archive обработку исключений.

Добавьте исключение в ваш код InvalidTextError, которые будет вызываться,
когда текст не является строкой или является пустой строкой.

И InvalidNumberError, которое будет вызываться,
если число не является положительным целым числом или числом с плавающей запятой.
"""
import traceback
from typing import Union


class MyBaseException(Exception):
    pass


class InvalidTextError(MyBaseException):
    """
    Вызывается когда текст не является строкой или является пустой строкой.
    """
    pass


class InvalidNumberError(MyBaseException):
    """
    Вызывается когда число не является положительным целым числом или числом с плавающей запятой.
    """
    pass


class Archive:
    """
    Класс, представляющий архив текстовых и числовых записей.

    Атрибуты:
    - archive_text (list): список архивированных текстовых записей.
    - archive_number (list): список архивированных числовых записей.
    - text (str): текущая текстовая запись для добавления в архив.
    - number (int или float): текущая числовая запись для добавления в архив.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
        return cls._instance

    def __init__(self, text: str, number: Union[int, float]):
        self.check_text(text)
        self._text = text
        self.check_number(number)
        self._number = number

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self.check_number(value)
        self._number = value

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self.check_text(value)
        self._text = value

    def check_text(self, text):
        """
        Вызывает ошибку InvalidTextError, если текст не является строкой или является пустой строкой.
        """
        if not isinstance(text, str) or text == "":
            self.cls_class()
            raise InvalidTextError(f"Invalid text: {text}. Text should be a non-empty string.")

    def check_number(self, number):
        """
        Вызывает ошибку InvalidNumberError, если число не является положительным целым числом или числом с плавающей запятой.
        """
        if number < 0:
            self.cls_class()
            raise InvalidNumberError(f"Invalid number: {number}. Number should be a positive integer or float.")

    def __str__(self):
        return f'Text is {self._text} and number is {self._number}. Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f'Archive("{self._text}", {self._number})'

    @staticmethod
    def cls_class():
        Archive._instance = None


def try_exec(*commands):
    for command in commands:
        try:
            print(f"Команда:\n{command}", "\n", "_" * 60)
            exec(command)
        except Exception as e:
            print(f"{e.__class__.__name__}: {e}")
        print()


if __name__ == '__main__':
    try_exec("""archive_instance = Archive("Sample text", 42.5)
print(archive_instance)""", """invalid_archive_instance = Archive("", -5)
print(invalid_archive_instance)""", """invalid_archive_instance = Archive("Sample text", -5)
print(invalid_archive_instance)""")
