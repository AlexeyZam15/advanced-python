"""
Создайте базовый класс Animal, который имеет атрибут name, представляющий имя животного.

Создайте классы Bird, Fish и Mammal, которые наследуются от базового класса Animal и добавляют дополнительные атрибуты и методы:

Bird имеет атрибут wingspan (размах крыльев) и метод wing_length, который возвращает длину крыла птицы.

Fish имеет атрибут max_depth (максимальная глубина обитания) и метод depth, который возвращает категорию глубины рыбы (мелководная, средневодная, глубоководная) в зависимости от значения max_depth.
Если максимальная глубина обитания рыбы (max_depth) меньше 10, то она относится к категории "Мелководная рыба".
Если максимальная глубина обитания рыбы больше 100, то она относится к категории "Глубоководная рыба".
В противном случае, рыба относится к категории "Средневодная рыба".

Mammal имеет атрибут weight (вес) и метод category, который возвращает категорию млекопитающего (Малявка, Обычный, Гигант) в зависимости от веса. Если вес объекта меньше 1, то он относится к категории "Малявка".
Если вес объекта больше 200, то он относится к категории "Гигант".
В противном случае, объект относится к категории "Обычный".

Создайте класс-фабрику AnimalFactory, который будет создавать экземпляры животных разных типов на основе переданного типа и параметров.
Класс-фабрика должен иметь метод create_animal, который принимает следующие аргументы:
animal_type (строка) - тип животного (один из: 'Bird', 'Fish', 'Mammal').
*args - переменное количество аргументов, представляющих параметры для конкретного типа животного.
Количество и типы аргументов могут различаться в зависимости от типа животного.
Метод create_animal должен создавать и возвращать экземпляр животного заданного типа с переданными параметрами.

Пример

На входе:


# Создание экземпляров животных
animal1 = AnimalFactory.create_animal('Bird', 'Орел', 200)
animal2 = AnimalFactory.create_animal('Fish', 'Лосось', 50)
animal3 = AnimalFactory.create_animal('Mammal', 'Слон', 5000)

# Вывод результатов
print(animal1.wing_length())
print(animal2.depth())
print(animal3.category())
На выходе:


100.0
Средневодная рыба
Гигант
"""


class Animal:
    """Базовый класс животного"""

    def __init__(self, name: str):
        """
        Конструктор класса Animal
        :param name: Имя животного
        """
        self.name = name


class Bird(Animal):
    """Класс птицы"""

    def __init__(self, name: str, wingspan):
        """
        Конструктор класса Bird
        :param name: Имя птицы
        :param wingspan: Размах крыла птицы
        """
        super().__init__(name)
        self.wingspan = wingspan

    def wing_length(self):
        """
        Метод wing_length, который возвращает длину крыла птицы.
        :return: Длина крыла птицы
        """
        return self.wingspan / 2.0


class Fish(Animal):
    """Класс рыбы"""

    def __init__(self, name: str, max_depth):
        """
        Конструктор класса Fish
        :param name: Имя рыбы
        :param max_depth: Максимальная глубина обитания рыбы
        """
        self.name = name
        self.max_depth = max_depth
        super().__init__(name)
        self.max_depth = max_depth

    def depth(self):
        """
Метод depth, который возвращает категорию глубины рыбы (мелководная, средневодная, глубоководная) в зависимости от значения max_depth.
Если максимальная глубина обитания рыбы (max_depth) меньше 10, то она относится к категории "Мелководная рыба".
Если максимальная глубина обитания рыбы больше 100, то она относится к категории "Глубоководная рыба".
В противном случае, рыба относится к категории "Средневодная рыба".
        :return: Тип рыбы по отношению к глубине
        """
        if self.max_depth < 10:
            return "Мелководная рыба"
        elif self.max_depth > 100:
            return "Глубоководная рыба"
        else:
            return "Средневодная рыба"


class Mammal(Animal):
    """Класс млекопитающего"""

    def __init__(self, name: str, weight):
        """
        Конструктор класса Mammal
        :param name: Имя млекопитающего
        :param weight: Вес млекопитающего
        :return: Нет
        """
        super().__init__(name)
        self.weight = weight

    def category(self):
        """
Метод category, который возвращает категорию млекопитающего (Малявка, Обычный, Гигант) в зависимости от веса.
Если вес объекта меньше 1, то он относится к категории "Малявка".
Если вес объекта больше 200, то он относится к категории "Гигант".
В противном случае, объект относится к категории "Обычный".
        :return: Размер млекопитающего
        """
        if self.weight < 1:
            return "Малявка"
        elif self.weight > 200:
            return "Гигант"
        else:
            return "Обычный"


class AnimalFactory:
    """Класс-фабрика для создания экземпляров животных разных типов"""
    @staticmethod
    def create_animal(animal_type: str, *args):
        """
        Создает экземпляр животного заданного типа с переданными параметрами.
        :param animal_type: Тип животного
        :param args: Параметры для создания экземпляра животного
        :return: Экземпляр животного заданного типа с переданными параметрами
        """
        if animal_type == 'Bird':
            return Bird(*args)
        elif animal_type == 'Fish':
            return Fish(*args)
        elif animal_type == 'Mammal':
            return Mammal(*args)

        raise ValueError("Недопустимый тип животного")


if __name__ == '__main__':
    animal1 = AnimalFactory.create_animal('Bird', 'Eagle', 200)
    print(animal1.wing_length())

    animal2 = AnimalFactory.create_animal('Fish', 'Salmon', 50)
    print(animal2.depth())

    animal3 = AnimalFactory.create_animal('Mammal', 'Elephant', 5000)
    print(animal3.category())

    animal4 = AnimalFactory.create_animal('Spider', 'Elephant', 5000)
    print(animal4.category())
