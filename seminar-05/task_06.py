"""
✔ Выведите в консоль таблицу умножения
от 2х2 до 9х10 как на школьной тетрадке.
✔ Таблицу создайте в виде однострочного
генератора, где каждый элемент генератора —
отдельный пример таблицы умножения.
✔ Для вывода результата используйте «принт»
без перехода на новую строку.
"""
from itertools import chain


# def multiplication_table(start: int, end: int) -> None:
#     max_indent = len(str(end * (end - 1)))
#     for i in range(start, end + 1):
#         for j in range(start, end // 2 + 1):
#             print(f"{j:>{max_indent * 3}} x {i:3} = {i * j:{max_indent}}", end="")
#         print()
#     print()
#     for i in range(start, end + 1):
#         for j in range(end // 2 + 1, end):
#             print(f"{j:>{max_indent * 3}} x {i:3} = {i * j:{max_indent}}", end="")
#         print()

def multiplication_table(start: int, end: int) -> None:
    max_indent = len(str(end * (end - 1)))
    for i in range(start, end + 1):
        text = ""
        for j in range(start, end // 2 + 1):
            text += f"{j:>{max_indent * 3}} x {i:3} = {i * j:{max_indent}}"
        yield text
    yield ""
    for i in range(start, end + 1):
        text = ""
        for j in range(end // 2 + 1, end):
            text += f"{j:>{max_indent * 3}} x {i:3} = {i * j:{max_indent}}"
        yield text


START = 2
END = 10

# print(*multiplication_table(START, END), sep="\n")

# mult_table = (f"{j} * {i} = {j * i}\t" if j != START else f"\n{j} * {i} = {j * i}\t" for i in range(START, END) for j in range(START, END))

max_indent = len(str(END * (END - 1)))

mult_table = chain(
    (
        f"{j:>{max_indent * 3}} x {i:3} = {i * j:{max_indent}}" if j != START else f"\n{j:>{max_indent * 3}} x {i:3} = {i * j:{max_indent}}"
        for i in range(START, END) for j in range(START, END // 2 + 1)), "\n\n", (
        f"{j:>{max_indent * 3}} x {i:3} = {i * j:{max_indent}}" if j != END // 2 + 1 else f"\n{j:>{max_indent * 3}} x {i:3} = {i * j:{max_indent}}"
        for i in range(START, END) for j in range(END // 2 + 1, END)))

print(*mult_table)
