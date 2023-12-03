import traceback


def func(a, b, c):
    if a < b < c:
        raise ValueError('Не перемешано!')
    elif sum((a, b, c)) == 42:
        raise NameError('Это имя занято!')
    elif max(a, b, c, key=len) < 5:
        raise MemoryError('Слишком глуп!')
    else:
        raise RuntimeError('Что-то не так!!!')


def try_exec(*commands):
    for i, command in enumerate(commands):
        try:
            exec(command)
        except Exception as e:
            print(f"Test {i + 1}", "\n", "_" * 60)
            print(e)

try_exec("func(11, 7, 3)", "func(3, 2, 3)", "func(73, -40, 9)", "func(10, 20, 30)")
