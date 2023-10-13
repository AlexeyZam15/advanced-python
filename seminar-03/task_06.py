"""Пользователь вводит строку текста. Вывести каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого длинного
слова был один пробел между ним и номером строки"""

text = input("Введите строку текста: ")

text_list = text.split()


def special_print(__list: list):
    sorted_list = sorted(__list)
    max_length_word = max([len(i) for i in sorted_list])

    print(*[f"{i + 1} {sorted_list[i]:>{max_length_word}}" for i in range(len(sorted_list))], sep="\n")


special_print(text_list)
