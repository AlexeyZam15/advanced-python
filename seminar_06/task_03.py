"""
� Улучшаем задачу 2.
� Добавьте возможность запуска функции “угадайки” из
модуля в командной строке терминала.
� Строка должна принимать от 1 до 3 аргументов: параметры
вызова функции.
� Для преобразования строковых аргументов командной
строки в числовые параметры используйте генераторное
выражение.
"""

from seminar_06.task_02 import guess_number

from sys import argv

try:
    guess_number(*(int(i) for i in argv[1:]))
except Exception as e:
    print(e)
