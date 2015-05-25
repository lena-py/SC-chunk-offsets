__author__ = 'lena'

import random
chunklist = []

def generate_random():
    randomnum = random.randrange(100)
    return randomnum

for i in range(50):
    if generate_random() >= 99:
        print("other ore")
        chunklist.append("other ore")
    else:
        print("granite")
        chunklist.append("granite")

print(chunklist)

for i in range(len(chunklist)):
    if chunklist[i] == "other ore":
        print(i)
print(len(chunklist))

chunklist2 = chunklist[:]
print(id(chunklist), id(chunklist2))

for i in range(len(chunklist)):
    if chunklist[i] == "other ore"

