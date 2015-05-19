__author__ = 'lena'
import struct
import binascii
print("NEW RUN")
# print a tuple of the hex number, stored as little endian
print(struct.unpack('<L', binascii.unhexlify('06010000')))
# hex equivalent of above
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




