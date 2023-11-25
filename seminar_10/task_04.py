"""
Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь
"""
from task_03 import Human


class Employer(Human):
    """
    Класс сотрудника.
    """

    def __init__(self, e_id: int, first_name: str, last_name: str, age: int):
        """
        Конструктор класса.
        :param e_id: Идентификационный номер
        :param first_name: Имя
        :param last_name: Фамилия
        :param age: Возраст
        """
        super().__init__(first_name, last_name, age)
        if e_id > 999999 or e_id < 100000:
            raise ValueError("Идентификационный номер должен состоять из 6 цифр")
        self.__e_id = e_id
        self.__access_level = sum([int(d) for d in str(e_id)]) % 7

    @property
    def e_id(self):
        """
        Получение идентификационного номера.
        :return: Идентификационный номер
        """
        return self.__e_id

    @property
    def access_level(self):
        """
        Получение уровня доступа.
        :return: Уровень доступа
        """
        return self.__access_level


if __name__ == '__main__':
    emp = Employer(123456, 'Иван', 'Иванов', 25)
    print(f"Идентификационный номер: {emp.e_id}")
    print(f"Уровень доступа: {emp.access_level}")
    print(f"ФИО сотрудника: {emp.full_name()}")
    print(f"Возраст сотрудника: {emp.age}")
