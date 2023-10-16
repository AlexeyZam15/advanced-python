"""
На вход подается словарь со списком вещей для похода в качестве ключа и их массой max_weight в качестве значения.
Определите какие вещи влезут в рюкзак backpack передав его максимальную грузоподъёмность.
В переменную backpack сохраните словарь {предмет:вес} с вещами в рюкзаке.
В переменную result выведите список, содержащий все возможные варианты backpack.
*Верните все возможные варианты комплектации рюкзака.
"""
import itertools
from pprint import pprint

items = {
    "ноутбук": 2.0,
    "книги": 1.5,
    "зарядное устройство": 0.5,
    "бутерброды": 0.3,
    "вода": 1.0
}
max_weight = 5.0

backpack = {}

keys = items.keys()


def weight_calculate(max_weight, items_names, items_dict):
    for i in items_names:
        max_weight -= items_dict[i]
    return max_weight > 0


result = []
for i in range(1, len(keys) + 1):
    for j in itertools.combinations(keys, i):
        backpack = {}
        if weight_calculate(max_weight, j, items):
            for k in j:
                backpack[k] = items[k]
            result.append(backpack)

print("[", end="")
print(*result, sep="\n", end="]\n")

# backpacks = []
#
# for i in range(2**len(items)):
#     backpack = {}
#     weight = 0
#     for j, item in enumerate(items):
#         if i & (1 << j):
#             if weight + items[item] <= max_weight:
#                 backpack[item] = items[item]
#                 weight += items[item]
#             else:
#                 break
#     backpacks.append(backpack)
#
# result = [backpack for backpack in backpacks if backpack]
#
# pprint(result)