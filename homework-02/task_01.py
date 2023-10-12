"""
Напишите программу, которая получает целое число num и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""

num = int(input('Введите число: '))


def hex_num(number: int):
    hex_number = ""
    hex_symbols = {10: "A",
                   11: "B",
                   12: "C",
                   13: "D",
                   14: "E",
                   15: "F", }
    while number > 0:
        hex_digit = number % 16
        hex_number = str(hex_digit if hex_digit < 10 else hex_symbols[hex_digit]) + hex_number
        number //= 16
    return hex_number


print("Шестнадцатеричное представление числа:", hex_num(num))
print("Проверка результата:", hex(num))
