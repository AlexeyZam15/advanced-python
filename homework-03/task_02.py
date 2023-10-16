"""В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.
Слова разделяются пробелами, апостроф не считается за пробел.
Такие слова как dont, its, didnt итд (после того, как убрали знак препинания апостроф) считать одним словом."""

text = ("Python is an interpreted, high-level, general-purpose programming language. "
        "Created by Guido van Rossum and first released in 1991, "
        "Python's design philosophy emphasizes code readability with its notable use of significant whitespace. "
        "Its language constructs and object-oriented approach aim to help programmers write clear, "
        "logical code for small and large-scale projects.")

formatted_text = (text.replace("'", " ").replace(".", "").replace(",", "")
                  .replace("!", "").replace("?", "").replace(":", "")
                  .replace(";", "").replace("-"," ").lower().split())

count_list = []

done = []

for i in formatted_text:
    if not i.isnumeric() and i not in done:
        count_list.append((i, formatted_text.count(i)))
        done.append(i)

count_list.sort(key=lambda x: x[1], reverse=True)
print(count_list[:10])
