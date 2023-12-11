"""
Дорабатываем задачу 4.
Добавьте возможность запуска из командной строки.
При этом значение любого параметра можно опустить. В
этом случае берётся первый в месяце день недели, текущий
день недели и/или текущий месяц.
*Научите функцию распознавать не только текстовое
названия дня недели и месяца, но и числовые,
т.е не мая, а 5.
"""
import argparse
import logging
from datetime import datetime

from task_04 import get_date

if __name__ == '__main__':
    file_name = __file__.split("\\")[-1]

    logger = logging.getLogger(file_name)

    FORMAT = 'уровень логирования: {levelname} - дата события: {asctime} - имя файла: {name}" ' \
             '{msg}'

    logging.basicConfig(level=logging.NOTSET,
                        format=FORMAT,
                        style="{",
                        filename=f"logs/{file_name.split('.')[0]}.log",
                        encoding="utf-8",
                        )

    date_time_now = datetime.now()
    parser = argparse.ArgumentParser(description=get_date.__doc__)
    parser.add_argument('-n', metavar='n_day', type=str,
                        help='введите номер дня недели в месяце', default="1")
    parser.add_argument('-wd', metavar='week_day', type=str,
                        help='введите день недели', default=date_time_now.weekday())
    parser.add_argument('-m', metavar='month', type=str,
                        help='введите месяц', default=date_time_now.month)
    args = parser.parse_args()
    date = get_date(f"{args.n} {args.wd} {args.m}")
    if isinstance(date, datetime):
        print(date.strftime("%d-%m-%Y"))
    else:
        print(date)
