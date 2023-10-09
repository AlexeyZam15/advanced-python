text = input("Введите текст: ")
if text.isdigit():
    print(bin(int(text)), oct(int(text)), hex(int(text)))
else:
    print("Текст написан в ASCII" if text.isascii() else "Текст не написан в ASCII")
