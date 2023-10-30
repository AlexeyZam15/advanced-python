"""
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
Под "успешной расстановкой ферзей" в данном контексте подразумевается такая расстановка ферзей на шахматной доске,
в которой ни один ферзь не бьет другого. Другими словами, ферзи размещены таким образом,
что они не находятся на одной вертикали, горизонтали или диагонали.
Список из 4х комбинаций координат сохраните в board_list. Дополнительно печатать его не надо.
"""

from random import choice

board_list = []


def is_attacking(q1: tuple, q2: tuple):
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])


def check_queens(queens: list):
    for i in range(len(queens) - 1):
        for j in range(i + 1, len(queens)):
            if is_attacking(queens[i], queens[j]):
                return False
    return True


def numbers_pairs(lower_start: int = 1, upper_start: int = 8):
    pairs = []
    for i in range(lower_start, upper_start + 1):
        for j in range(lower_start, upper_start + 1):
            if (i, j) not in pairs:
                pairs.append((i, j))
    return pairs


def generate_boards():
    while len(board_list) < 4:
        board = []
        pairs = numbers_pairs()
        while len(board) < 8 and pairs:
            pair = choice(pairs)
            pairs.remove(pair)
            board.append(pair)
            if not check_queens(board):
                board.remove(pair)
        if len(board) == 8 and board not in board_list:
            board_list.append(board)
    return board_list


generate_boards()
print("Решение")
print(*board_list, sep="\n")


def print_board(chess_positions: list):
    print("_" * 60)
    print("  ", end="")
    for j in range(8):
        print(f" {j + 1} ", end="")
    print()
    for i in range(1, 8 + 1):
        print(i, end=" ")
        for j in range(1, 8 + 1):
            if (i, j) in chess_positions:
                print("|Q|", end="")
            else:
                print("| |", end="")
        print()


# import random
# from itertools import combinations
#
#
# def generate_board():
#     # Генерируем случайную доску
#     board = []
#
#     for i in range(1, 8 + 1):
#         queen = (i, random.randint(1, 8))
#         board.append(queen)
#     return board
#
#
# def is_attacking(q1, q2):
#     # Проверяем, бьют ли ферзи друг друга
#     return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])
#
#
# def check_queens(queens):
#     # Проверяем все возможные пары ферзей
#     for q1, q2 in combinations(queens, 2):
#         if is_attacking(q1, q2):
#             return False
#     return True
#
#
# def generate_boards():
#     # Генерируем доски, пока не получим 4 успешные расстановки
#     count = 0
#     board_list = []
#     while count < 4:
#         board = generate_board()
#         print(board)
#         if check_queens(board):
#             count += 1
#             board_list.append(board)
#     return board_list


board_list = generate_boards()

for board in board_list:
    print_board(board)
