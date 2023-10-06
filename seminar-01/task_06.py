"""
Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
"""


def create_mult_table(start_num, end_num):
    mult_table = []
    for i in range(start_num, end_num):
        column = ""
        for j in range(start_num, end_num + 1):
            column += f'{i} * {j:2} = {i * j:2}\n'
        mult_table.append(column)
    return mult_table


def print_mult_table(mult_table: list):
    print(f"{'ТАБЛИЦА УМНОЖЕНИЯ':>45}")
    text_row_1 = ""
    text_row_2 = ""
    for i in range(len(mult_table) + 1):
        for col in range(len(mult_table) // 2):
            rows = mult_table[col].split("\n")
            text_row_1 += f'{rows[i]:20}'
        text_row_1 += "\n"

        for col in range(len(mult_table) // 2, len(mult_table)):
            rows = mult_table[col].split("\n")
            text_row_2 += f'{rows[i]:20}'
        text_row_2 += "\n"
    print(text_row_1, text_row_2, sep="\n")


START = 2
END = 10

mult_table = create_mult_table(START, END)

print_mult_table(mult_table)
