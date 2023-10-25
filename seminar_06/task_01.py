"""
� Вспомните какие модули вы уже проходили на курсе.
� Создайте файл, в котором вы импортируете встроенные в
модуль функции под псевдонимами. (3-7 строк импорта).
"""

from sys import argv as ar
from os import getcwd as cwd
from math import sqrt as sq
from random import random as rnd

print(ar)
print(cwd())
print(sq(4))
print(rnd())
