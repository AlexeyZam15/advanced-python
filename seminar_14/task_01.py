"""
Создайте функцию, которая удаляет из текста все символы
кроме букв латинского алфавита и пробелов.
Возвращается строка в нижнем регистре.
"""


def only_latins_text(text: str):
    """
    Удаляет из текста все символы кроме букв латинского алфавита и пробелов
    :param text: Входящий текст
    :return: Обработанный текст в нижнем рекистре
    """
    return ''.join(filter(lambda x: x in 'abcdefghijklmnopqrstuvwxyz ', text.lower()))


if __name__ == '__main__':
    print(only_latins_text('Hello, World!'))
    print(only_latins_text('Здравствуйте, Мир!'))
