"""
Напишите для задачи 1 тесты pytest. Проверьте следующие
варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
"""

from pytest import main
from task_01 import only_latins_text


def test_case_1():
    assert only_latins_text("abcdefghijklmnopqrstuvwxyz ") == 'abcdefghijklmnopqrstuvwxyz '


def test_case_2():
    assert only_latins_text("ABCD ") == 'abcd '


def test_case_3():
    assert only_latins_text("a,b.c?d") == 'abcd'


def test_case_4():
    assert only_latins_text("aаbбcсdвeеfфgг") == 'abcdefg'


def test_case_5():
    assert only_latins_text("AА,BБ.CС?DД") == 'abcd'


if __name__ == '__main__':
    main(['-v'])
