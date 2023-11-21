"""
Создайте декоратор с параметром.
Параметр - целое число, количество запусков декорируемой
функции.
"""
from typing import Callable


def run_times(times: int):
    res_list = []

    def run_func(func: Callable):
        def wrapper(*args):
            for _ in range(times):
                res_list.append(func(*args, *res_list))
            return res_list

        return wrapper

    return run_func


@run_times(13)
def add_sum(*args):
    return sum(args)


if __name__ == '__main__':
    print(add_sum(2))
