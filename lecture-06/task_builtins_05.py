import random as rnd

data = [2, 4, 6, 8, 42, 73]

print(data)
rnd.shuffle(data)
print(data)
print(rnd.sample(data, 2))
print(rnd.sample(data, 2, counts=[1, 1, 1, 1, 1, 100]))
