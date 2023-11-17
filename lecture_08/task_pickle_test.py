import pickle

my_dict = {'numbers': [42, 4.1415, (7 + 3j)],
           'functions': (sum, max),
           'others': {False, True, 'Hello world!'}
           }

res = pickle.dumps(my_dict)
with open('quest.pickle', 'wb') as f:
    pickle.dump(f'{res = }', f)

with open('quest.pickle', 'rb') as f:
    print(f.read())

with open('quest.pickle', 'rb') as f:
    data = pickle.load(f)
print(data)

"""выделить из data байты"""
data_bytes = data.split(" = ")
print(data_bytes)
"""выполнить строку"""
data_bytes = eval(data_bytes[1])
print(pickle.loads(data_bytes))
