"""
Создайте класс с базовым исключением и дочерние классы исключения:
○ ошибка уровня,
○ ошибка доступа.
"""
import traceback


class MyBaseException(Exception):
    pass


class LevelError(MyBaseException):
    def __init__(self, required_level):
        self.required_level = required_level
        self.level = 0

    def __call__(self, level):
        self.level = level
        if level < self.required_level:
            raise self

    def __str__(self):
        if self.level >= self.required_level:
            return "Доступ разрешён"
        return f"Ошибка уровня - уровень {self.level} меньше необходимого уровня ({self.required_level})"


class AccessError(MyBaseException):
    def __init__(self, required_access):
        self.required_access = required_access
        self.access = ""

    def __call__(self, access):
        self.access = access
        if access != self.required_access:
            raise self

    def __str__(self):
        if self.access == self.required_access:
            return "Доступ разрешён"
        return f"Ошибка доступа: {self.access}. Требуется допуск {self.required_access}"


def try_exec(command, exception):
    try:
        exec(command)
    except exception as e:
        print(f"{exception.__name__}: {e}")


if __name__ == '__main__':
    level_error = LevelError(10)
    try_exec("level_error(5)", LevelError)
    access_error = AccessError("admin")
    try_exec("access_error('user')", AccessError)
