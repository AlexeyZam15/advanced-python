"""
Доработаем задачу 2.
Сохраняйте в лог файл раздельно:
○ уровень логирования,
○ дату события,
○ имя функции (не декоратора),
○ аргументы вызова,
○ результат
"""

import logging


def log_all(func):
    file_name = __file__.split("\\")[-1]

    logger = logging.getLogger(file_name)

    def wrapper(*args):
        FORMAT = 'уровень логирования: {levelname} - дата события: {asctime} - имя файла: {name}" ' \
                 '- номер строки: {lineno:03d} - ' \
                 f'имя функции: {func.__name__}' \
                 '{msg}'

        logging.basicConfig(level=logging.NOTSET,
                            format=FORMAT,
                            style="{",
                            filename=f"logs/{file_name.split('.')[0]}.log",
                            encoding="utf-8",
                            filemode="w"
                            )

        try:
            result = func(*args)
            logger.info(f' - аргументы функции: {args} - результат работы функции: {result}')
        except Exception as e:
            logger.error(f' - аргументы функции: {args} - результат работы функции: {e.__class__.__name__}: {e}')
            result = "Ошибка"
        return result

    return wrapper


@log_all
def divide(a, b):
    return a / b


if __name__ == '__main__':
    divide(20, 5)
    divide(1, 0)
