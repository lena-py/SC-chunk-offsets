# HEX CHECKS
# a = int("10410", base=16)
# print(a)
#
# b = int("c000c", base=16)
# print(b)
#
# c = int("0xd041c", base=16)
#
# print(b % a)
# print(hex(c % a))

# DATA VALIDATION
# import string
#
#
# def check_iterations(any_iterations):
#     print(len(any_iterations))
#     idx = 0
#     i = 0
#     found = 0
#
#     while i < len(any_iterations):
#         while idx < 10:
#             print("idx", idx, "i", i)
#             if any_iterations[i] == string.digits[idx]:
#                 found += 1
#                 print("found")
#                 idx = 10
#
#             else:
#                 idx += 1
#                 print("notfound")
#         i += 1
#         idx = 0
#         print("round")
#
#     print(found)
#     if found == len(any_iterations):
#         found = True
#     else:
#         found = False
#     return found
#
# print(check_iterations(str("nnn")))

# STRING DIGITS
# import string
#
# for i in range(len(string.hexdigits)):
#
#     print(string.hexdigits[i])

from ChunkOffsets import valid_entry

import string

s = "12345"
print(len(s))
i = 0
found = 0

while i < len(s):
    if s[i] in string.hexdigits:
        found += 1
    i += 1

print("found is", found)


def lePack(n, l):
    """ Converts integer to bytes. If length after conversion
    is smaller than given as param returned value is right-filled
    with 0x00 bytes. Use Little-endian byte order."""
    return b''.join([
        chr((n >> ((l - i - 1) * 8)) % 256) for i in xrange(l)
    ][::-1])



lePack(256, 8)
