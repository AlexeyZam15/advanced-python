my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.get('two'))
print(my_dict.get('five'))
# получить значение по ключу или заданное значение по умолчанию
print(my_dict.get('five', 5))
print(my_dict.get('ten', 5))