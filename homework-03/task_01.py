"""На вход подается словарь со списком вещей для похода в качестве ключа и их массой max_weight в качестве значения.
Определите какие вещи влезут в рюкзак backpack передав его максимальную грузоподъёмность.
Результат должен быть в виде словаря {предмет:вес} с вещами в рюкзаке и сохранен в переменную backpack.
Достаточно вернуть один допустимый вариант."""

items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}

max_weight = 1.0

backpack = dict()

for i in items:
    if max_weight > items[i]:
        backpack[i] = items[i]
        max_weight -= items[i]

print(backpack)
