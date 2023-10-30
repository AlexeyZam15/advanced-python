import shutil

ONE_TXT = 'one.txt'
TWO_TXT = 'two.txt'

with open(ONE_TXT, mode="a") as one:
    print(ONE_TXT, file=one)
with open(TWO_TXT, mode="a") as two:
    print(TWO_TXT, file=two)

shutil.copy(ONE_TXT, 'dir')

# копирует мета-данные
shutil.copy2(TWO_TXT, 'dir')
