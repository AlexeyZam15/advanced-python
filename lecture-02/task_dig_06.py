DEFAULT = 42
num = int(input('Введите уровень или 0 для значения по умолчанию:'))
level = num or DEFAULT
print(level)
