"""
В организации есть два типа людей: сотрудники и обычные люди.
Каждый человек (и сотрудник, и обычный) имеет следующие атрибуты:

Фамилия (строка, не пустая) Имя (строка, не пустая) Отчество (строка, не пустая) Возраст (целое положительное число)
Сотрудники имеют также уникальный идентификационный номер (ID), который должен быть шестизначным положительным целым числом.

Ваша задача:

Создать класс Person,
который будет иметь атрибуты и методы для управления данными о людях (Фамилия, Имя, Отчество, Возраст).
Класс должен проверять валидность входных данных и генерировать исключения InvalidNameError и InvalidAgeError,
если данные неверные.

Создать класс Employee, который будет наследовать класс Person и добавлять уникальный идентификационный номер (ID).
Класс Employee также должен проверять валидность ID и генерировать исключение InvalidIdError, если ID неверный.

Добавить метод birthday в класс Person, который будет увеличивать возраст человека на 1 год.

Добавить метод get_level в класс Employee, который будет возвращать уровень сотрудника
на основе суммы цифр в его ID (по остатку от деления на 7).

Создать несколько объектов класса Person и Employee с разными данными и проверить,
что исключения работают корректно при передаче неверных данных.
"""


class MyBaseException(Exception):
    pass


class InvalidNameError(MyBaseException):
    """
    Вызывается когда текст не является строкой или является пустой строкой.
    """
    pass


class InvalidAgeError(MyBaseException):
    """
    Вызывается когда число не является положительным целым числом или числом с плавающей запятой.
    """
    pass


class InvalidIdError(MyBaseException):
    """
    Вызывается когда число не является шестизначным положительным целым числом или числом с плавающей запятой.
    """
    pass


class Person:
    """
    Класс Person,
    который имеет атрибуты и методы для управления данными о людях (Фамилия, Имя, Отчество, Возраст).
    Класс проверяет валидность входных данных и генерирует исключения InvalidNameError и InvalidAgeError,
    если данные неверные.
    """

    def __init__(self, last_name, first_name, middle_name, age):
        self._last_name = last_name
        self._first_name = first_name
        self._middle_name = middle_name
        self._age = age

    @property
    def middle_name(self):
        return self._middle_name

    @middle_name.setter
    def middle_name(self, value):
        self.check_name(value)
        self._middle_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self.check_name(value)
        self._last_name = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self.check_name(value)
        self._first_name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self.check_age(value)
        self._age = value

    def __new__(cls, last_name, first_name, middle_name, age):
        cls.check_name(last_name)
        cls.check_name(first_name)
        cls.check_name(middle_name)
        cls.check_age(age)
        return super().__new__(cls)

    @staticmethod
    def check_name(value):
        """
        Вызывает ошибку InvalidTextError, если текст не является строкой или является пустой строкой.
        """
        if not isinstance(value, str) or value == "":
            raise InvalidNameError(f"Invalid name: {value}. Name should be a non-empty string.")

    @staticmethod
    def check_age(value):
        """
        Вызывает ошибку InvalidNumberError, если число не является положительным целым числом или числом с плавающей
        запятой.
        """
        if value < 0:
            raise InvalidAgeError(f"Invalid age: {value}. Age should be a positive integer.")

    def birthday(self):
        """
        Метод birthday, который увеличивает возраст человека на 1 год.
        """
        self._age += 1

    def __str__(self):
        return f'Last name: {self._last_name}, First name: {self._first_name}, Middle name: {self._middle_name}, Age: {self._age}'

    def get_age(self):
        return self._age


class Employee(Person):
    """
    Класс Employee, который наследуется от класса Person и добавляет уникальный идентификационный номер (ID).
    Класс Employee также проверяет валидность ID и генерирует исключение InvalidIdError, если ID неверный.
    """

    def __init__(self, last_name, first_name, middle_name, age, e_id):
        super().__init__(last_name, first_name, middle_name, age)
        self._e_id = e_id

    @property
    def e_id(self):
        return self._e_id

    @e_id.setter
    def e_id(self, value):
        self.check_id(value)
        self._e_id = value

    def __new__(cls, last_name, first_name, middle_name, age, e_id):
        cls.check_id(e_id)
        return super().__new__(cls, last_name, first_name, middle_name, age)

    @staticmethod
    def check_id(value):
        """
        Проверка id на шестизначное положительное целое число
        """
        if not isinstance(value, int) or value < 0 or len(str(value)) != 6:
            raise InvalidIdError(
                f"Invalid id: {value}. Id should be a 6-digit positive integer between 100000 and 999999.")

    def get_level(self):
        """
        Метод get_level, который возвращает уровень сотрудника
        на основе суммы цифр в его ID (по остатку от деления на 7).
        """
        return sum([int(digit) for digit in str(self._e_id)]) % 7

    def __str__(self):
        return f'{super().__str__()}, ID: {self._e_id}, Level: {self.get_level()}'


def try_exec(*commands):
    for command in commands:
        try:
            print(f"Команда:\n{command}", "\n", "_" * 60)
            exec(command)
        except Exception as e:
            print(f"{e.__class__.__name__}: {e}")
        print()


if __name__ == '__main__':
    try_exec("""person = Person("", "John", "Doe", 30)
print()""", """
person = Person("Alice", "Smith", "Johnson", -5)
print()""", """
employee = Employee("Bob", "Johnson", "Brown", 40, 12345)
print()""", """
person = Person("Alice", "Smith", "Johnson", 25)
print(person.get_age())
""")
