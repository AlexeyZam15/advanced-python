"""
Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса.
"""
"""
Доработайте задачу 5.
Вынесите общие свойства и методы классов в класс
Животное.
Остальные классы наследуйте от него.
Убедитесь, что в созданные ранее классы внесены правки
"""


class Animal:
    def __init__(self, name: str):
        self.name = name

    def info(self):
        print(f'Animal: {self.name}')


class Fish(Animal):
    def __init__(self, name: str, red_fish: bool):
        super().__init__(name)
        self.__red_fish = red_fish

    def info(self):
        print(f'Red fish: {self.name}' if self.__red_fish else f"White fish: {self.name}")


class Bird(Animal):
    def __init__(self, name: str, can_fly: bool):
        super().__init__(name)
        self.__can_fly = can_fly

    def info(self):
        print(f'Flying bird: {self.name}' if self.__can_fly else f'Not flying bird: {self.name}')


class Mammal(Animal):
    def __init__(self, name: str, big: bool):
        super().__init__(name)
        self.__big = big

    def info(self):
        print(f'Big mammal: {self.name}' if self.__big else f'Small mammal: {self.name}')


if __name__ == '__main__':
    animal = Animal('Crocodile')
    fish = Fish("Salmon", True)
    bird = Bird('Penguin', False)
    mammal = Mammal('Tiger', True)

    animal.info()
    fish.info()
    bird.info()
    mammal.info()
