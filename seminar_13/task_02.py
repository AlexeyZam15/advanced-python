"""
Создайте функцию аналог get для словаря.
Помимо самого словаря функция принимает ключ и
значение по умолчанию.
При обращении к несуществующему ключу функция должна
возвращать дефолтное значение.
Реализуйте работу через обработку исключений.
"""


def get_dict(dict_, key, default):
    try:
        return dict_[key]
    except KeyError:
        return default


if __name__ == '__main__':
    data = {'one': 1, 'two': 2}
    print(f"{get_dict(data, 'one', 0) = }")
    print(f"{get_dict(data, 'two', 0) = }")
    print(f"{get_dict(data, 'three', 0) = }")
