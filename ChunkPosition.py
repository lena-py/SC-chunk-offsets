__author__ = 'lena'
import struct
import binascii

print("NEW RUN")


def offset(xhexnum, zhexnum, rel):

    for i in range(1, rel+1, 1):
        hexasbyte = binascii.unhexlify(xhexnum)
        byteunpack = struct.unpack('<L', hexasbyte)
        newint = byteunpack[0] + i
        newbytepack = struct.pack("I", newint)
        newbyteashex = binascii.hexlify(newbytepack)
        print(newbyteashex, end="")
        hexasbyte = binascii.unhexlify(zhexnum)
        byteunpack = struct.unpack('<L', hexasbyte)
        newint = byteunpack[0] + i
        newbytepack = struct.pack("I", newint)
        newbyteashex = binascii.hexlify(newbytepack)
        print(newbyteashex)


offset('06010000', '82000000', 10)











