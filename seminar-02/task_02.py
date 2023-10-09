"""
Создайте в переменной data список значений разных типов перечислив их через
запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
✔ порядковый номер начиная с единицы
✔ значение
✔ адрес в памяти
✔ размер в памяти
✔ хэш объекта
✔ результат проверки на целое число только если он положительный
✔ результат проверки на строку только если он положительный.
Добавьте в список повторяющиеся элементы и сравните на результаты.
"""


def exec_task(data: list):
    for i in range(len(data)):
        print(i, data[i], id(data[i]), data[i].__sizeof__(), hash(data[i]),
              isinstance(data[i], int) if isinstance(data[i], int) else "",
              isinstance(data[i], str) if isinstance(data[i], str) else "")
    print("_" * 50)


data = [1, "string", True, None, 1.1, (1, 2, 3)]
exec_task(data)

data += [1, "string", True, None, 1.1, (1, 2, 3)]
exec_task(data)
