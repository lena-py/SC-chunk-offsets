__author__ = 'lena'

import random
chunklist = []


def generate_random():
    randomnum = random.randrange(100)
    return randomnum

print("ANOTHER RUN")
# Create initial chunk column
for i in range(50):
    if generate_random() >= 99:
        chunklist.append("other ore")
    else:
        chunklist.append("granite")

# Traverse the column to increase the "other ore"
for i in range(len(chunklist)):
    # Print the idx of "other ore"
    if 0 < i < 49 and chunklist[i] == "other ore":
        chunklist[i-1] = "other ore"
print(chunklist)
print(chunklist.count("other ore"))

# Create second column
chunklist2 = chunklist[:]