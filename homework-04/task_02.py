"""
Напишите функцию key_params, принимающую на вход только ключевые параметры
и возвращающую словарь, где ключ - значение переданного аргумента, а значение - имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
"""
import typing


def key_params(**kwargs):
    dict_ = {}
    for i in kwargs:
        if isinstance(kwargs[i], typing.Hashable):
            dict_[kwargs[i]] = i
        else:
            dict_[str(kwargs[i])] = i
    return dict_


print(key_params(a=None, b='', c=[], d={}))
