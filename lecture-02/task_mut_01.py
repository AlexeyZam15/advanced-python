a = 5
print(a, id(a))
a += 1
print(a, id(a))

txt = "Hello world!"
try:
    txt[5] = '_'
except Exception as e:
    print(e)

txt = "Hello world!"
print(txt, id(txt))
txt = txt.replace(' ', '_')
print(txt, id(txt))
