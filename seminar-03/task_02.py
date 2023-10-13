"""Пользователь вводит данные. Сделайте проверку данных
и преобразуйте если возможно в один из вариантов ниже:
✔ Целое положительное число
✔ Вещественное положительное или отрицательное число
✔ Строку в нижнем регистре, если в строке есть
хотя бы одна заглавная буква
✔ Строку в нижнем регистре в остальных случаях"""

data = input("Введите данные: ")

if data.isdigit():
    print("Данные преобразованы в целое положительное число")
# проверка строки на Вещественное положительное или отрицательное число
elif data.replace('.', '', 1).replace("-", "", 1).isdigit():
    print("Данные преобразованы в вещественное положительное или отрицательное число")
    data = float(data)
# проверка в строке есть хотя бы одна заглавная буква
elif any(x.isupper() for x in data):
    print("Данные преобразованы в cтроку в нижнем регистре, т.к. в строке есть хотя бы одна заглавная буква")
    data = data.lower()
else:
    print("Данные преобразованы в строку в нижнем регистре")
    data = data.lower()

print(data)
