"""✔ Пользователь вводит строку текста.
✔ Подсчитайте сколько раз встречается
каждая буква в строке без использования
метода count и с ним.
✔ Результат сохраните в словаре, где ключ —
символ, а значение — частота встречи
символа в строке.
✔ Обратите внимание на порядок ключей.
Объясните почему они совпадают
или не совпадают в ваших решениях."""

text = input("Введите текст: ")

symbols_repeats_dict = {}

for i in text:
    if i not in symbols_repeats_dict:
        symbols_repeats_dict[i] = 1
    else:
        symbols_repeats_dict[i] += 1

print(symbols_repeats_dict)

symbols_count_dict = {}
for i in text:
    if i not in symbols_count_dict:
        symbols_count_dict[i] = text.count(i)

print(symbols_repeats_dict)
