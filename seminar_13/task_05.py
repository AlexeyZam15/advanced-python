"""
Доработаем задачи 3 и 4. Создайте класс проекта, который
имеет следующие методы:
загрузка данных (функция из задания 4)
вход в систему - требует указать имя и id пользователя. Для
проверки наличия пользователя в множестве используйте
магический метод проверки на равенство пользователей.
Если такого пользователя нет, вызывайте исключение
доступа. А если пользователь есть, получите его уровень из
множества пользователей.
добавление пользователя. Если уровень пользователя
меньше, чем ваш уровень, вызывайте исключение уровня
доступа.
"""
import json


class MyBaseException(Exception):
    pass


class LevelError(MyBaseException):
    def __init__(self, text="Ошибка уровня"):
        self.text = text

    def __str__(self):
        return self.text


class IdError(MyBaseException):
    def __init__(self, text="Такой id уже существует"):
        self.text = text

    def __str__(self):
        return self.text


class AccessError(MyBaseException):
    def __init__(self, text="Ошибка доступа"):
        self.text = text

    def __str__(self):
        return self.text


class User:
    def __init__(self, access_level, user_id, name):
        self.access_level = access_level
        self.user_id = user_id
        self.name = name

    def __str__(self):
        return f"User {self.user_id} ({self.name}) has access level {self.access_level}"

    def __eq__(self, other):
        """
        Метод для проверки равенства пользователей.
        """
        if isinstance(other, tuple):
            if self.user_id == other[0] and self.name == other[1]:
                return True
        if isinstance(other, User):
            if self.user_id == other.user_id and self.name == other.name:
                return True
        return False


class Project:
    def __init__(self, json_file):
        self.users = self.read_users(json_file)
        self.level = 0

    def __call__(self):
        self.level = self.sign_in()
        self.add_user()

    @staticmethod
    def read_users(json_file):
        """
        Загрузка данных из json файла
        """
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        created_users = []
        for access_level, users in data.items():
            for user_id, name in users.items():
                created_users.append(User(access_level, user_id, name))
        return created_users

    def sign_in(self):
        """
        Вход в систему - требует указать имя и id пользователя. Для
проверки наличия пользователя в множестве используйте
магический метод проверки на равенство пользователей.
Если такого пользователя нет, вызывает исключение
доступа. А если пользователь есть, получает его уровень из
множества пользователей.
        :return: Уровень пользователя
        """
        name = input("Укажите имя пользователя: ")
        user_id = input("Укажите id пользователя: ")
        user = self.get_user(user_id, name)
        if user is None:
            raise AccessError("Пользователя с указанными id и именем не существует")
        return int(user.access_level)

    def get_user(self, user_id, name):
        for user in self.users:
            if user == (user_id, name):
                return user
        return None

    def get_user_by_id(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def add_user(self):
        """
        Добавление пользователя. Если уровень пользователя
меньше, чем ваш уровень, вызывает исключение уровня
доступа.
        """
        print("Укажите данные для нового пользователя")
        level = int(input("Укажите уровень: "))
        if level < self.level:
            raise LevelError("Ваш уровень должен быть больше или равен уровня создаваемого пользователя")
        user_id = input("Укажите id пользователя: ")
        if self.get_user_by_id(user_id):
            raise IdError("Пользователь с таким id уже существует")
        name = input("Укажите имя пользователя: ")
        new_user = User(level, user_id, name)
        self.users.append(new_user)
        return new_user


if __name__ == '__main__':
    JSON_FILE = "task_04.json"
    p = Project(JSON_FILE)
    p()
    print(*p.users, sep="\n")
