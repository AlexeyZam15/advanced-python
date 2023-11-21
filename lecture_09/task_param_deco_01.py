import time
from typing import Callable


def count(num: int = 1):
    def deco(func: Callable):
        _cache_dict = {}

        def wrapper(*args, **kwargs):
            time_for_count = []
            result = None
            for _ in range(num):
                start = time.perf_counter()
                if args not in _cache_dict:
                    _cache_dict[args] = func(*args, **kwargs)
                result = _cache_dict[args]
                stop = time.perf_counter()
                time_for_count.append(stop - start)
            print(f'Результаты замеров {time_for_count}')
            return result

        return wrapper

    return deco


@count(3)
def factorial(n: int) -> int:
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


print(f'{factorial(1000) = }')
print(f'{factorial(1000) = }')
