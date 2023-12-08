"""
Напишите для задачи 1 тесты doctest. Проверьте
следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
"""


def only_latins_text(text: str):
    """
    Удаляет из текста все символы кроме букв латинского алфавита и пробелов
    :param text: Входящий текст
    :return: Обработанный текст в нижнем рекистре
    >>> only_latins_text("abcdefghijklmnopqrstuvwxyz ")
    'abcdefghijklmnopqrstuvwxyz '
    >>> only_latins_text("ABCD ")
    'abcd '
    >>> only_latins_text("a,b.c?d")
    'abcd'
    >>> only_latins_text("aаbбcсdвeеfфgг")
    'abcdefg'
    >>> only_latins_text("AА,BБ.CС?DД")
    'abcd'
    """
    return ''.join(filter(lambda x: x in 'abcdefghijklmnopqrstuvwxyz ', text.lower()))


if __name__ == '__main__':
    from doctest import testmod
    testmod(verbose=True)
