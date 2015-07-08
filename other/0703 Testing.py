__author__ = 'lena'
from datetime import datetime
import binascii


# use multiplieriplier on the lookup value
marble = b'4400'
keys = ['chunk1.dat', 'chunk2.dat', 'chunk3.dat']
templates = {marble*2: 'Chunk2.dat'}

print(templates[b'44004400'])


# Recursive algorithm for lookup values?
chunk = b'440044004400'


def lookup(achunk, code, multiplier):
    value = code * multiplier
    if achunk.count(value) > 0:
        return multiplier
    else:
        multiplier -= 1
        return lookup(achunk, code, multiplier)


startTime = datetime.now()
print(lookup(chunk, marble, 14))
print(datetime.now() - startTime)

# The original way
count = 1
startTime = datetime.now()
if chunk.count(b'44004400440044004400440044004400') > 0:
    count = 18
elif chunk.count(b'4400440044004400440044004400') > 0:
    count = 7
elif chunk.count(b'440044004400440044004400') > 0:
    count = 6
elif chunk.count(b'44004400440044004400') > 0:
    count = 5
elif chunk.count(b'4400440044004400') > 0:
    count = 4
elif chunk.count(b'440044004400') > 0:
    count = 3
elif chunk.count(b'44004400') > 0:
    count = 2

print(count)
print(datetime.now() - startTime)


# Using a for loop
startTime = datetime.now()
multiplier = 14
for i in range(14):
    value = marble * multiplier
    if chunk.count(value) > 0:
        print(multiplier)
        break
    multiplier -= 1
print(datetime.now() - startTime)


# Testing just overwriting the open file rather than making the list!
outfile = open("Chunk_out2.dat", "wb")
with open("Chunk_out.dat", "rb") as f:
    test = f.read(12)
    hexed_test = binascii.hexlify(test)
    replace = b'D4'
    hexed_test = hexed_test.replace(b'b4', replace)
    print(hexed_test)
    outfile.write(binascii.unhexlify(hexed_test))

outfile.close()

outfile2 = open("Chunk_out3.dat", "wb")
with open("Chunk_out.dat", "rb") as f:
    test = f.read()
    replace = b'\xd4'
    find = test.find(b'\x44\x00\x44')
    new_test = test.replace(b'\xb4', replace)
    # print(new_test)
    outfile2.write(new_test)

outfile2.close()
print("done")
print(find)

