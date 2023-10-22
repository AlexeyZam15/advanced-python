"""
✔ Создайте генератор чётных чисел от нуля до 100.
✔ Из последовательности исключите
числа, сумма цифр которых равна 8.
✔ Решение в одну строку.
"""

# even_nums_gen = (i for i in range(101) if i % 2 == 0 and sum([int(j) for j in str(i)]) != 8)

even_nums_gen = (i for i in range(0, 101, 2) if sum([int(j) for j in str(i)]) != 8)

print(*even_nums_gen)
