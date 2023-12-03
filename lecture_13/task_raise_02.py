import traceback


class User:
    def __init__(self, name, age):
        if 6 < len(name) < 30:
            self.name = name
        else:
            raise ValueError(f'Длина имени должна быть между 6 и 30 символами. {len(name) = }')
        if not isinstance(age, (int, float)):
            raise TypeError(f'Возраст должен быть числом. Используйте int или float. {type(age) = }')
        elif age < 0:
            raise ValueError(f'Возраст должен быть положительным. {age = }')
        else:
            self.age = age

    def __repr__(self):
        return f'User(name={self.name}, age={self.age})'


def try_exec(command):
    try:
        exec(command)
    except Exception:
        traceback.print_exc()
        return False
    else:
        return True


try_exec("User('Яков', '-12')")
try_exec("User('Яковлев', '-12')")
try_exec("User('Яковлев', -12)")
try_exec("print(User('Яковлев', 12))")
