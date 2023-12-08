"""
Напишите для задачи 1 тесты unittest. Проверьте
следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
"""
from unittest import TestCase, main

from seminar_14.task_01 import only_latins_text


class Task01Test(TestCase):
    def test_case_1(self):
        self.assertEqual(only_latins_text("abcdefghijklmnopqrstuvwxyz "), 'abcdefghijklmnopqrstuvwxyz ')

    def test_case_2(self):
        self.assertEqual(only_latins_text("ABCD "), 'abcd ')

    def test_case_3(self):
        self.assertEqual(only_latins_text("a,b.c?d"), 'abcd')

    def test_case_4(self):
        self.assertEqual(only_latins_text("aаbбcсdвeеfфgг"), 'abcdefg')

    def test_case_5(self):
        self.assertEqual(only_latins_text("AА,BБ.CС?DД"), 'abcd')


if __name__ == '__main__':
    main()
