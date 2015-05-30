## THIS IS UGLY CODE


def hex2dec(num):
    """
    convert a hex value in base 16 to an int
    :param num: a hex value in string format
    :return: converted value
    """
    dec = int(num, base=16)

    return dec

test_values = ["10410", "c000c", "d041c"]
for i in range(len(test_values)):
    print("test_value as < class int > ", hex2dec(test_values[i]))

remainder = hex2dec(test_values[1]) % hex2dec(test_values[0])
print("remainder of offset / chunk:", remainder)
print("remainder formatted as hex: {:X}".format(remainder))


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
#
# from ChunkOffsets import valid_entry
#
# import string
#
# s = "12345"
# print(len(s))
# i = 0
# found = 0
#
# while i < len(s):
#     if s[i] in string.hexdigits:
#         found += 1
#     i += 1
#
# print("found is", found)
#
# __author__ = 'lena'
# import struct
# import binascii
# print("NEW RUN")
#
#
# def hex_unhex():
#     # from inner method
#     # binascii.unhexlify: Return the binary data represented by the hexadecimal string hexstr.
#     # struct.unpack: Unpack from the buffer buffer (presumably packed by pack(fmt, ...)) according to the format string fmt.
#     # output is a tuple
#     print(struct.unpack('<L', binascii.unhexlify('06010000')))
#     # hex equivalent of above
#     # uses an index to access the first element of the tuple
#     print(hex(struct.unpack('<L', binascii.unhexlify('06010000'))[0]))
#     # pack an int
#     print(struct.pack("I", 262))
#
#
#     a = (binascii.unhexlify('06010000'))
#     print("a is", a)
#
#     a1 = struct.pack("I", struct.unpack('<L', a)[0] + 1)
#     print("a1 is", a1)
#     print("a1 type is", type(a1))
#
#     b = binascii.hexlify(a)
#     print("b is", b)
#
#     c = struct.unpack('<L', a1)
#     print(c[0])
#     print(hex(c[0]))
#
# hex_unhex()
'----------------------------------------------------------------------------------------------------------------------'

#
# with open("chunks.dat", "rb") as f:
#     byte = f.read(4)
#     chunklist = [[], [], []]
#     print(byte)
#     for num in range(630):
#         for i in range(3):
#             b = binascii.hexlify(byte)
#
#             print(struct.unpack('<L', binascii.unhexlify(b)))
#             b = struct.unpack('<L', binascii.unhexlify(b))
#             b = b[0]
#             chunklist[i].append(b)
#
#             byte = f.read(4)
#
#
# print(chunklist)
# coords = []
# for num in range(630):
#     coord = [chunklist[0][num], chunklist[1][num]]
#     coords.append(coord)
# print(coords)
# i = 0
# for acoord in coords:
#     print(acoord)
#     repeats = (coords.count(acoord))
#     print(repeats)
#     if repeats > 1:
#         print("eureka")
#         print(i)
#         break
#     i += 1

