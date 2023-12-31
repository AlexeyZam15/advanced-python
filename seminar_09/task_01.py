"""
Создайте функцию-замыкание, которая запрашивает два целых числа:
○ от 1 до 100 для загадывания,
○ от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток.
"""


def guess_number():
    number = input("Загадайте число от 1 до 100: ")
    while 1 >= int(number) >= 100:
        print("Введено неверное число")
        number = input("Загадайте число от 1 до 100: ")

    attempts = int(input("Введите кол-во попыток для отгадывания от 1 до 10: "))
    while 1 >= attempts >= 10:
        print("Введено неверное число")
        attempts = int(input("Введите кол-во попыток для отгадывания от 1 до 10: "))

    def input_number():
        for attempt in range(attempts, 0, -1):
            print(f"Попробуйте отгадать число, осталось попыток: {attempt}")
            input_num = input("Введите число: ")
            if input_num == number:
                print("Число угадано")
                return
            print("Неверно")
        print("Попытки кончились, число не угадано")
        return

    return input_number

if __name__ == '__main__':
    guess = guess_number()
    guess()
