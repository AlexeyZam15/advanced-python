"""
Напишите программу, которая использует модуль logging для
вывода сообщения об ошибке в файл.
Например отлавливаем ошибку деления на ноль.
"""

import logging

FORMAT = '{levelname} - {asctime}. В модуле "{name}" ' \
         'в строке {lineno:03d} функция "{funcName}()" записала сообщение: {msg}'

logging.basicConfig(filename="logs/task_01.log",
                    encoding="utf-8",
                    filemode="w",
                    level=logging.ERROR,
                    format=FORMAT,
                    style="{"
                    )

logger = logging.getLogger(__file__.split("\\")[-1])


def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        logger.error(f"Деление {n1} на {n2} вызвало ошибку деления на ноль")
        print(f"Ошибка: деление {n1} на {n2} вызвало ошибку деления на ноль")


divide(1, 0)
