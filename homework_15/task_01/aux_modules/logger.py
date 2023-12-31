import logging
import os
from functools import wraps

from aux_modules.exceptions import MyBaseException
import inspect


def log_all(func):
    file_name = inspect.getfile(func).split("\\")[-1]

    logger = logging.getLogger(file_name)

    @wraps(func)
    def wrapper(*args):
        FORMAT = '{levelname} - дата события: {asctime}" ' \
                 '{msg}'
        logging.basicConfig(level=logging.NOTSET,
                            format=FORMAT,
                            style="{",
                            filename="/".join(inspect.getfile(func).split("\\")[0:-1]) + f"/logs/{file_name.split('.')[0]}.log",
                            encoding="utf-8",
                            )
        try:
            result = func(*args)
            logger.info(f' - имя функции: {func.__name__}'
                        f' - аргументы функции: {args} - результат работы функции: {result}')
            return result
        except MyBaseException as e:
            logger.error(f' - имя функции: {func.__name__}'
                         f' - аргументы функции: {args} - результат работы функции: {e.__class__.__name__}: {e}'
                         f' - ошибка в строке: {e.error_line}, в файле {e.file_name}')
            # result = f"{e.__class__.__name__}: {e}"

    return wrapper
