"""
На семинаре про декораторы был создан логирующий
декоратор. Он сохранял аргументы функции и результат её
работы в файл.
Напишите аналогичный декоратор, но внутри используйте
модуль logging.
"""

import logging
from functools import wraps

logger = logging.getLogger(__file__.split("\\")[-1])


def log_all(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        FORMAT = '{levelname} - {asctime}. В модуле "{name}" ' \
                 'в строке {lineno:03d} функция ' \
                 f'"{func.__name__}"' \
                 ' записала сообщение: {msg}'

        logging.basicConfig(level=logging.NOTSET,
                            format=FORMAT,
                            style="{",
                            filename="logs/task_02.log",
                            encoding="utf-8",
                            filemode="w"
                            )

        try:
            result = func(*args, **kwargs)
        except Exception as e:
            logger.error(f"{e.__class__.__name__}: {e}")
            result = "Ошибка"
        logger.info(f'Аргументы функции: {args}, {kwargs}')
        logger.info(f'Результат работы функции: {result}')
        return result

    return wrapper


@log_all
def divide(a, b):
    return a / b


divide(1, 0)
