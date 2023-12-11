"""
Функция получает на вход текст вида: “1-й четверг ноября”, “3-
я среда мая” и т.п.
Преобразуйте его в дату в текущем году.
Логируйте ошибки, если текст не соответствует формату.
"""
import logging
import sys

from datetime import datetime, timedelta
from functools import wraps
from dicts import *


class MyBaseException(Exception):
    def __init__(self, str):
        self.str = str
        exc_type, exc_obj, exc_tb = sys.exc_info()
        self.error_line = exc_tb.tb_lineno
        super().__init__(self.str)


class InvalidDayError(MyBaseException):
    pass


class InvalidMonthError(MyBaseException):
    pass


class InvalidDayWeekError(MyBaseException):
    pass


def log_all(func):
    file_name = __file__.split("\\")[-1]

    logger = logging.getLogger(file_name)

    @wraps(func)
    def wrapper(*args):
        FORMAT = 'уровень логирования: {levelname} - дата события: {asctime} - имя файла: {name}" ' \
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
            logger.info(f' - имя функции: {func.__name__}'
                        f' - аргументы функции: {args} - результат работы функции: {result}')
        except MyBaseException as e:
            logger.error(f' - имя функции: {func.__name__}'
                         f' - аргументы функции: {args} - результат работы функции: {e.__class__.__name__}: {e}'
                         f' - номер строки - {e.error_line}')
            result = f"{e.__class__.__name__}: {e}"
        return result

    return wrapper


@log_all
def get_date(date_text: str):
    """
    Функция получает на вход текст вида: “1-й четверг ноября”, “3-
я среда мая” и т.п.
Преобразуйте его в дату в текущем году.
Логируйте ошибки, если текст не соответствует формату.
    """
    date_text = date_text.lower()
    date_text_split = date_text.split()
    n_day = date_text_split[0].split("-")[0]
    try:
        n_day = int(n_day)
    except ValueError:
        raise InvalidDayError(f"{n_day} - число дня недели должно быть целым числом")
    past_week_days = 0
    month = date_text_split[2]
    if month in en_to_ru_months:
        month = datetime.strptime(month, "%B").month
    elif month in ru_to_en_months:
        month = datetime.strptime(ru_to_en_months[month], "%B").month
    elif month.isdigit() and int(month) in range(1, 13):
        month = int(month)
    else:
        try:
            raise KeyError
        except KeyError:
            raise InvalidMonthError(f"{month} - неверное название месяца")

    datetime_now = datetime.now().replace(day=1,
                                          month=month,
                                          hour=0, minute=0, second=0, microsecond=0)
    weekday = date_text_split[1]
    if weekday in en_to_ru_week_days:
        weekday = week_days_numbers[weekday]
    elif weekday in ru_to_en_week_days:
        weekday = week_days_numbers[ru_to_en_week_days[weekday]]
    elif weekday.isdigit() and int(weekday) in range(7):
        weekday = int(weekday)
    else:
        try:
            raise KeyError
        except KeyError:
            raise InvalidDayWeekError(f"{weekday} - неверное название дня недели")
    td = timedelta(hours=24)

    while True:
        if datetime_now.weekday() == weekday:
            past_week_days += 1
        if past_week_days >= n_day:
            break
        datetime_now += td
        if datetime_now.month != month:
            try:
                raise ValueError
            except ValueError:
                raise InvalidDayError(f"{n_day} - неверное число дня недели в месяце")
    return datetime_now


def from_date_to_date_name(date: datetime):
    """
    Функция преобразует дату в текст вида: “2 ноября 2023”
    """
    month = months_numbers[date.month]
    return date.strftime(f'%d {month} %Y').replace(month, en_to_ru_months[month])


def get_key_by_value(dict_: dict, value):
    """
    Функция возвращает ключ по значению
    """
    for key, v in dict_.items():
        if v == value:
            return key
    return None


if __name__ == '__main__':
    enquiries = ["1-й четверг ноября", "3-я среда мая", "5-й вторник мая", "7-я суббота июля",
                 "9-е воскресенье августа", "dfgdfg fgdfg dfg fdg", "1 fgdfg dfg fdg", "1 gfhfgh ноября",
                 "24-ый четверг ноября", "1 monday november"]

    for enquiry in enquiries:
        date = get_date(enquiry)
        if isinstance(date, datetime):
            print(f'{enquiry} = {date.strftime("%d-%m-%Y")} = {from_date_to_date_name(date)}')
