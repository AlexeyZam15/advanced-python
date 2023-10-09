"""
Напишите программу, которая получает целое число и возвращает
его двоичное, восьмеричное строковое представление.
✔ Функции bin и oct используйте для проверки своего
результата, а не для решения.
Дополнительно:
✔ Попробуйте избежать дублирования кода
в преобразованиях к разным системам счисления.
✔ Избегайте магических чисел.
✔ Добавьте аннотацию типов, где это возможно.
"""


def convert_to_base(number: int, base: int, prefix: str = None):
    converted_num: str = ""
    while number > 0:
        converted_num = str(number % base) + converted_num
        number //= base
    return prefix + converted_num


NUMBER: int = 332

converted_to_bin_number: str = convert_to_base(NUMBER, 2, "0b")
bin_number: str = bin(NUMBER)

print(converted_to_bin_number, bin_number, converted_to_bin_number == bin_number)

converted_to_oct_number: str = convert_to_base(NUMBER, 8, "0o")
oct_number: str = oct(NUMBER)

print(converted_to_oct_number, oct_number, converted_to_oct_number == oct_number)
