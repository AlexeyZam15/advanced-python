"""
На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.

Напишите программу, которая должна возвращать сумму и произведение дробей.

Для проверки своего кода используйте модуль fractions.
"""

from fractions import Fraction

import math

frac1 = input("Введите первую дробь: ")
frac2 = input("Введите вторую дробь: ")


def str_fractions_to_int(fraction: str):
    numerator, denominator = fraction.split('/')
    return int(numerator), int(denominator)


def fractional_reduction(numerator: int, denominator: int):
    # алгоритм сокращения дроби
    if numerator == denominator:
        return 1
    elif numerator == 0:
        return 0

    gcd = math.gcd(numerator, denominator)
    numerator //= gcd
    denominator //= gcd
    return str(numerator) if denominator == 1 else f"{numerator}/{denominator}"


def fractions_sum(fraction_1: str, fraction_2: str):
    # алгоритм суммы дробей
    numerator_1, denominator_1 = str_fractions_to_int(fraction_1)

    numerator_2, denominator_2 = str_fractions_to_int(fraction_2)

    res_numerator = numerator_1 * denominator_2 + numerator_2 * denominator_1

    res_denominator = denominator_1 * denominator_2

    return f"{fractional_reduction(res_numerator, res_denominator)}"


def fractions_mult(fraction_1: str, fraction_2: str):
    # алгоритм произведения дробей
    numerator_1, denominator_1 = str_fractions_to_int(fraction_1)

    numerator_2, denominator_2 = str_fractions_to_int(fraction_2)

    res_numerator = numerator_1 * numerator_2
    res_denominator = denominator_1 * denominator_2

    return f"{fractional_reduction(res_numerator, res_denominator)}"


print("Сумма дробей:", fractions_sum(frac1, frac2))
print("Произведение дробей:", fractions_mult(frac1, frac2))

print("Сумма дробей:", Fraction(frac1) + Fraction(frac2))
print("Произведение дробей:", Fraction(frac1) * Fraction(frac2))
