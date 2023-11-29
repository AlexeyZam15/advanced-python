"""
Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При создании нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списков архивов
list-архивы также являются свойствами экземпляра
"""


class Archive:
    """Класс архив, для хранения чисел и строк"""
    old_archive_nums = []
    old_archive_strings = []

    __instance = None

    def __init__(self, number, string):
        """
        Инициализация архива с передачей числа и строки.
        Если архив уже создан, то данные из предыдущих архивов сохраняются в пару списков архивов.
        :param number: Число
        :param string: Строка
        """
        self.number = number
        self.string = string

    def __new__(cls, number, string):
        """
        Создание нового экземпляра класса и сохранение данных из предыдущих архивов.
        Если архив уже создан, то данные из предыдущих архивов сохраняются в пару списков архивов.
        :param number: Число
        :param string: Строка
        """
        if cls.__instance:
            cls.old_archive_strings.append(cls.__instance.string)
            cls.old_archive_nums.append(cls.__instance.number)

        cls.__instance = super().__new__(cls)

        return cls.__instance


if __name__ == '__main__':
    a = Archive(1, 'Первый')
    b = Archive(2, 'Второй')
    c = Archive(3, 'Третий')
    d = Archive(4, 'Четвертый')
    print(f'{a.number = }, {a.string = }')
    print(f'{b.number = }, {b.string = }')
    print(f'{c.number = }, {c.string = }')
    print(f'{d.number = }, {d.string = }')
    print(f'{Archive.old_archive_nums = }')
    print(f'{Archive.old_archive_strings = }')
