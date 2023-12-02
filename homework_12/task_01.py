"""
Создайте класс студент:
○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
Если ФИО не соответствует условию,
выведите:
ФИО должно состоять только из букв и начинаться с заглавной буквы

○ Названия предметов должны загружаться из файла CSV при создании экземпляра.
Другие предметы в экземпляре недопустимы. Если такого предмета нет, выведите:
Предмет {Название предмета} не найден

○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
В противном случае выведите:
Оценка должна быть целым числом от 2 до 5

Результат теста должен быть целым числом от 0 до 100
○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
Вам предоставлен файл subjects.csv, содержащий предметы. Сейчас в файл записана следующая информация.
Математика,Физика,История,Литература

Создайте класс Student, который будет представлять студента и его успехи по предметам. Класс должен иметь следующие методы:
Атрибуты класса:
name (str): ФИО студента. subjects (dict): Словарь, который хранит предметы в качестве ключей и информацию об оценках и результатах тестов для каждого предмета в виде словаря.

Магические методы (Dunder-методы):
__init__(self, name, subjects_file): Конструктор класса. Принимает имя студента и файл с предметами и их результатами.
Инициализирует атрибуты name и subjects и вызывает метод load_subjects для загрузки предметов из файла.

__setattr__(self, name, value): Дескриптор, который проверяет установку атрибута name.
Убеждается, что name начинается с заглавной буквы и состоит только из букв.

__getattr__(self, name): Позволяет получать значения атрибутов предметов (оценок и результатов тестов) по их именам.

__str__(self): Возвращает строковое представление студента, включая имя и список предметов.
Студент: Иван Иванов
Предметы: Математика, История

Методы класса:
load_subjects(self, subjects_file): Загружает предметы из файла CSV.
Использует модуль csv для чтения данных из файла и добавляет предметы в атрибут subjects.

add_grade(self, subject, grade): Добавляет оценку по заданному предмету.
Убеждается, что оценка является целым числом от 2 до 5.

add_test_score(self, subject, test_score): Добавляет результат теста по заданному предмету.
Убеждается, что результат теста является целым числом от 0 до 100.

get_average_test_score(self, subject): Возвращает средний балл по тестам для заданного предмета.

get_average_grade(self): Возвращает средний балл по всем предметам.

Пример

На входе:
student = Student("Иван Иванов", "subjects.csv")

student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)

student.add_grade("История", 5)
student.add_test_score("История", 92)

average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")

average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике: {average_test_score}")

print(student)

На выходе:
Средний балл: 4.5
Средний результат по тестам по математике: 85.0
Студент: Иван Иванов
Предметы: Математика, История
"""
import csv
import traceback


class Validator:
    def __init__(self, conditions: dict):
        self.conditions = conditions

    def __set_name__(self, owner, name):
        self.param_name = "_" + name

    def validate(self, value):
        for k, v in self.conditions.items():
            for i in value.split():
                if k(i) is False:
                    raise ValueError(v)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)


class Student:
    name = Validator({str.isalpha: "ФИО должно состоять только из букв и начинаться с заглавной буквы",
                      str.istitle: "ФИО должно состоять только из букв и начинаться с заглавной буквы"})

    def __init__(self, name, subjects_file):
        """
        __init__(self, name, subjects_file): Конструктор класса.
        Принимает имя студента и файл с предметами и их результатами.
        Инициализирует атрибуты name и subjects и вызывает метод load_subjects для загрузки предметов из файла.
        :param name: Имя студента
        :param subjects_file: Файл с предметами
        """

        self.name = name
        self.subjects = {}

        self.subjects = self.load_subjects(subjects_file)

        self.exist_subjects = []

        self.grades = {k: [] for k in self.subjects}
        self.test_score = {k: [] for k in self.subjects}

    @staticmethod
    def load_subjects(subjects_file):
        """
        load_subjects: Загружает предметы из файла CSV.
Использует модуль csv для чтения данных из файла и добавляет предметы в атрибут subjects.
        :param subjects_file: файл csv
        :return: список прочитанных значений из csv файла
        """
        with open(subjects_file, "r", encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)
            subjects = []
            for row in reader:
                for subject in row:
                    if subject not in subjects:
                        subjects.append(subject)
        return subjects

    def __str__(self):
        """
        __str__: Возвращает строковое представление студента, включая имя и список предметов.
Студент: Иван Иванов
Предметы: Математика, История
        """
        return f"Студент: {self.name}\nПредметы: {', '.join(self.exist_subjects)}"

    def check_subject(self, subject):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден")

    def add_grade(self, subject, grade):
        """
        add_grade(self, subject, grade): Добавляет оценку по заданному предмету.
        Убеждается, что оценка является целым числом от 2 до 5.
        :param subject: Название предмета
        :param grade: Оценка - целое число от 2 до 5
        """
        if grade not in range(2, 6) or not isinstance(grade, int):
            raise ValueError("Оценка должна быть целым числом от 2 до 5")
        self.check_subject(subject)
        if subject not in self.exist_subjects:
            self.exist_subjects.append(subject)
        self.grades[subject].append(grade)

    def add_test_score(self, subject, test_score):
        """
        add_test_score(self, subject, test_score): Добавляет результат теста по заданному предмету.
    Убеждается, что результат теста является целым числом от 0 до 100.
        :param subject: Название предмета
        :param test_score: Результаты теста - число от 0 до 100
        """
        if test_score not in range(0, 101) or not isinstance(test_score, int):
            raise ValueError("Результаты теста должны быть целым числом от 0 до 100.")
        self.check_subject(subject)
        if subject not in self.exist_subjects:
            self.exist_subjects.append(subject)
        self.test_score[subject].append(test_score)

    def get_average_test_score(self, subject):
        """
        get_average_test_score(self, subject): Возвращает средний балл по тестам для заданного предмета.
        :param subject: Название предмета
        """
        self.check_subject(subject)
        return round(sum(self.test_score[subject]) / len(self.test_score[subject]), 1)

    def get_average_grade(self):
        """
        get_average_grade(self): Возвращает средний балл по всем предметам.
        """
        return round(sum(sum(self.grades.values(), [])) / sum(len(v) for v in self.grades.values()), 1)


if __name__ == '__main__':
    print("Test 1", "\n", "-" * 60)
    student = Student("Иван Иванов", "subjects.csv")

    student.add_grade("Математика", 4)
    student.add_test_score("Математика", 85)

    student.add_grade("История", 5)
    student.add_test_score("История", 92)

    average_grade = student.get_average_grade()
    print(f"Средний балл: {average_grade}")

    average_test_score = student.get_average_test_score("Математика")
    print(f"Средний результат по тестам по математике: {average_test_score}")

    print(student)
    print("Test 2", "\n", "-" * 60)
    try:
        student = Student("123 Иван", "subjects.csv")
    except Exception as e:
        print(e)
    print("Test 3", "\n", "-" * 60)
    student = Student("Петров Петр", "subjects.csv")
    try:
        student.add_grade("Физика", 6)
    except Exception as e:
        print(e)
    print("Test 4", "\n", "-" * 60)
    student = Student("Сидоров Сидор", "subjects.csv")
    try:
        average_history_score = student.get_average_test_score("Биология")
    except Exception as e:
        print(e)
