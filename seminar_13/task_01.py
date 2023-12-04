"""
Создайте функцию, которая запрашивает числовые данные от
пользователя до тех пор, пока он не введёт целое или
вещественное число.
Обрабатывайте не числовые данные как исключения.
"""


def get_number():
    while True:
        number = input("Введите вещественное или целое число: ")
        try:
            return int(number)
        except ValueError:
            try:
                return float(number)
            except ValueError as ve:
                print(f"Ошибка")


if __name__ == '__main__':
    number = get_number()
    print(f"Введённое число = {number}")
