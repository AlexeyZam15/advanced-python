"""
Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст.
"""


class Human:
    """Класс для хранения информации о человеке"""

    def __init__(self, first_name: str, last_name: str, age: int, middle_name: str = ""):
        """
        Конструктор класса Human

        :param middle_name: Отчество
        :param last_name:  Фамилия
        :param age: Возраст
        :param first_name: Имя
        """
        self.__first_name = first_name
        self.__middle_name = middle_name
        self.__last_name = last_name
        self.__age = age

    @property
    def middle_name(self):
        """
        Получение отчества
        :return: отчество
        """
        return self.__middle_name

    @property
    def first_name(self):
        """
        Получение имени
        :return: Имя
        """
        return self.__first_name

    @property
    def age(self):
        """
        Получение возраста
        :return: Возраст
        """
        return self.__age

    @property
    def last_name(self):
        """
        Получение фамилии
        :return: Фамилия
        """
        return self.__last_name

    def birthday(self):
        """
        Увеличение возраста на 1 год
        :return: Возраст
        """
        self.__age += 1
        return self.__age

    def full_name(self):
        """
        Вывод полного имени
        :return: ФИО
        """
        return f"{self.__first_name} {self.__middle_name} {self.__last_name}"


if __name__ == '__main__':
    human = Human("Иван", "Иванов", 25, "Иванович")
    print(human.full_name())
    print(human.age)
    print(human.birthday())
    print(human.full_name())
    print(human.first_name)
    print(human.middle_name)
    print(human.last_name)
