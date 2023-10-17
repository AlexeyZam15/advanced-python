"""
✔ Создайте несколько переменных c названиями заканчивающихся и не оканчивающихся на «s».
✔ Напишите функцию, которая при запуске заменяет содержимое переменных
оканчивающихся на s (кроме переменной из одной буквы s) на None.
✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
"""

x = 'x'
s = 'xs'
xs_s = 'xs_s'
xs_s_s = 'xs_s_s'


def replace_multiple_s(**kwargs):
    for i in kwargs:
        if i.endswith("s") and len(i) > 1:
            name = i[:-1]
            globals()[name] = kwargs[i]
            globals()[i] = None


replace_multiple_s(x=x, s=s, xs_s=xs_s, xs_s_s=xs_s_s)
print(*filter(lambda x: not x[0].startswith('__'), globals().items()), sep="\n")
