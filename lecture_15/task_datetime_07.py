import locale
from datetime import datetime

locale.setlocale(locale.LC_ALL, ('ru_RU', 'UTF-8'))

dt = datetime(year=2007, month=6, day=15, hour=2, minute=14, microsecond=24)
print(dt)
print(dt.timestamp())
print(dt.isoformat())
print(dt.weekday())
print(dt.strftime('Дата %d %B %Y. День недели %A. Время %H:%M:%S. Это %W неделя и %j день года.'))
