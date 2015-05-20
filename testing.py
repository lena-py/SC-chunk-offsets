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

__author__ = 'lena'
import struct
import binascii
print("NEW RUN")
# from inner method
# binascii.unhexlify: Return the binary data represented by the hexadecimal string hexstr.
# struct.unpack: Unpack from the buffer buffer (presumably packed by pack(fmt, ...)) according to the format string fmt.
# output is a tuple
print(struct.unpack('<L', binascii.unhexlify('06010000')))
# hex equivalent of above
# uses an index to access the first element of the tuple
print(hex(struct.unpack('<L', binascii.unhexlify('06010000'))[0]))
# pack an int
print(struct.pack("I", 262))


a = (binascii.unhexlify('06010000'))
print("a is", a)

a1 = struct.pack("I", struct.unpack('<L', a)[0] + 1)
print("a1 is", a1)
print("a1 type is", type(a1))

b = binascii.hexlify(a)
print("b is", b)

c = struct.unpack('<L', a1)
print(c[0])
print(hex(c[0]))





