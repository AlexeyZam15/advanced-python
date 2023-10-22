# Создайте функцию генератор чисел Фибоначчи fibonacci.

def fibonacci():
    pre = 0
    last = 1
    while True:
        yield pre
        pre, last = last, pre + last


f = fibonacci()
for i in range(10):
    print(next(f))
