"""На вход программе подаются два списка, каждый из которых содержит 10 различных целых чисел.
Первый список ваш лотерейный билет.
Второй список содержит список чисел, которые выпали в лотерею.
Вам необходимо определить и вывести количество совпадающих чисел в этих двух списках.

Напишите класс LotteryGame, который будет иметь метод compare_lists,
который будет сравнивать числа из вашего билета из list1 со списком выпавших чисел list2

Если совпадающих чисел нет, то выведите на экран: Совпадающих чисел нет.
Пример входных данных:

list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]

game = LotteryGame(list1, list2)
matching_numbers = game.compare_lists()

Пример выходных данных:
Совпадающие числа: [3, 12, 8, 41, 9, 14, 5]
Количество совпадающих чисел: 7
"""


class LotteryGame:
    def __init__(self, list_1: list, list_2: list):
        self.list_1 = list_1
        self.list_2 = list_2

    def compare_lists(self):
        matching_nums = []
        for i in self.list_1:
            if i in self.list_2:
                matching_nums.append(i)
        if matching_nums:
            print("Совпадающие числа:", matching_nums)
            print("Количество совпадающих чисел:", len(matching_nums))
        else:
            print("Совпадающих чисел нет.")
        return matching_nums


if __name__ == '__main__':
    list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
    list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]

    game = LotteryGame(list1, list2)
    matching_numbers = game.compare_lists()

    list1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    list2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    game = LotteryGame(list1, list2)
    matching_numbers = game.compare_lists()

    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    game = LotteryGame(list1, list2)
    matching_numbers = game.compare_lists()
