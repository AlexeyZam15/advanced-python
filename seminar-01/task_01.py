"""
Задание №4.
Решите квадратное уравнение
5x2-10x-400=0 последовательно
сохраняя переменные a, b, c, d, x1 и x2.
*Попробуйте решить уравнения с другими значениями a, b, c.
"""


def solve_quadratic_equation(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return x1, x2
    elif d == 0:
        x = -b / (2 * a)
        return x
    else:
        return None


def print_solutions(solutions):
    if solutions is None:
        print("Уравнение не имеет решений")
    elif isinstance(solutions, tuple):
        print(f"x1 = {solutions[0]}, x2 = {solutions[1]}")
    else:
        print(f"x = {solutions}")


a = int(input("Введите значение a: "))
b = int(input("Введите значение b: "))
c = int(input("Введите значение c: "))
solutions = solve_quadratic_equation(a, b, c)
print_solutions(solutions)
