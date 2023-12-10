from datetime import time, date, datetime

d = date(year=2007, month=6, day=15)
t = time(hour=2, minute=14, second=0, microsecond=24)
dt = datetime(year=2007, month=6, day=15, hour=2, minute=14, second=0, microsecond=24)
print(f'{d = } - {d}')
print(f'{t = } - {t}')
print(f'{dt = } - {dt}')
