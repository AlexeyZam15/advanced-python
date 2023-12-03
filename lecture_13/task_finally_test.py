d = {'42': 73}
try:
    key, value = input('Ключ и значение: ').split()
    if d[key] == value:
        r = 'Совпадение'
except ValueError as e:
    print(f"ValueError: {e}")
except KeyError as e:
    print(f"KeyError: {e}")
else:
    print(r)
finally:
    print(d)