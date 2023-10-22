"""
✔ Создайте функцию-генератор.
✔ Функция генерирует N простых чисел,
начиная с числа 2.
✔ Для проверки числа на простоту используйте
правило: «число является простым, если делится
нацело только на единицу и на себя».
"""


def prime_numbers(n: int):
    start_number = 2
    count = 0
    for i in range(start_number, n):
        prime = True
        # for j in range(start_number, i // 2 + 1):
        #     if i % j == 0:
        #         prime = False
        #         break
        if any(i % j == 0 for j in range(start_number, i)):
            prime = False
        if prime:
            count += 1
            yield i
    print(count)


N = 1000

print(*prime_numbers(N), "\n")
