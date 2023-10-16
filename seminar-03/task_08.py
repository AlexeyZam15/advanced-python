"""✔ Три друга взяли вещи в поход. Сформируйте
словарь, где ключ — имя друга, а значение —
кортеж вещей. Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного
и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции
с множествами. Код должен расширяться
на любое большее количество друзей."""

friends_items_dict = {
    "Петя": ("кепка", "ножик", "тетрадка", "ручка", "зажигалка", "вино"),
    "Вася": ("кепка", "ножик", "булка хлеба", "мармелад"),
    "Алексей": ("сосиски", "вино", "мармелад")
}

# all_items_set = set()
# for friend in friends_items_dict:
#     for item in friends_items_dict[friend]:
#         all_items_set.add(item)
# print("Все вещи:", ", ".join(all_items_set))

print("Все вещи, которые взяли все три друга.", end=f'\n{"_" * 60}\n')
for i in friends_items_dict:
    print(f"{i} взял: ", end="")
    print(", ".join(friends_items_dict[i]))

unique_items = set()
all_items = set()
for i in friends_items_dict.values():
    for j in i:
        all_items.add(j)
        if j in unique_items:
            unique_items.remove(j)
        else:
            unique_items.add(j)
print("_" * 60)
print("Уникальные вещи:", ", ".join(unique_items))

common_items = all_items - unique_items

dont_have_items = dict()
for i in common_items:
    count = len(friends_items_dict)
    poor_friend = None
    for friend in friends_items_dict:
        if i in friends_items_dict[friend]:
            count -= 1
        else:
            poor_friend = friend
    if count == 1:
        if poor_friend not in dont_have_items:
            dont_have_items[poor_friend] = []
        dont_have_items[poor_friend].append(i)

for i in dont_have_items:
    print(f"Только у {i} нету: ", ", ".join(dont_have_items[i]))
