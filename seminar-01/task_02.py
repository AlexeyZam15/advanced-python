"""
Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
Используйте while и if.
Попробуйте разные значения e и n
"""

n = int(input('Введите число: '))
e = int(input('Введите число e: '))
i = 1
sum_values = 0
numbers = []

while i <= n:
    if i % 2 == 0 and i % e != 0:
        sum_values += i
        numbers.append(i)
    i += 1

print(f'Сумма чисел от 1 до {n} исключая кратные {e}: {sum_values}')
print(f'Числа от 1 до {n} исключая кратные {e}: {numbers}')
