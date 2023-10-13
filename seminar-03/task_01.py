"""✔ Вручную создайте список с целыми числами, которые
повторяются. Получите новый список, который содержит
уникальные (без повтора) элементы исходного списка.
✔ *Подготовьте два решения, короткое и длинное, которое
не использует другие коллекции помимо списков."""

my_list = [1, 2, 3, 1, 2, 3, 4, 5, 6]
print(my_list)
my_list1 = my_list.copy()

my_list = list(set(my_list))
print(my_list)

delete_list = []
for i in range(len(my_list1)):
    if my_list1[i] in my_list1[i + 1:]:
        delete_list.append(my_list1[i])
for i in delete_list:
    my_list1.remove(i)
print(my_list1)
