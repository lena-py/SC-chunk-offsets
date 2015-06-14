# THIS IS UGLY CODE
import binascii
import struct


def list_attributes(item):
    attributes = [item, type(item), len(item), item[0], type(item[0])]
    count = 0
    for i in ("value:", "type:", "length", "b[0]", "type[b[0]"):
        print(i, attributes[count])
        count += 1
    print('-----------')

    return


def read_bytes(file, openformat):
    with open(file, openformat) as f:
        somebytes = f.read(4)

    return somebytes


def hexlify_bytes(somebytes):
    b = binascii.hexlify(somebytes)

    return b


def main():
    bytecycle = (read_bytes("chunks.dat", "rb"))
    present_as_hex = hexlify_bytes(bytecycle)
    unpacked = struct.unpack('L', present_as_hex)

    list_attributes(bytecycle)
    list_attributes(present_as_hex)
    list_attributes(unpacked)

if __name__ == '__main__':
    main()
#
# chunklist = [[], [], []]
# for num in range(700):
#     for i in range(3):
#         b = binascii.hexlify(byte)
#         #print(b)
# #
# #             print(struct.unpack('<L', binascii.unhexlify(b)))
# #             b = struct.unpack('<L', binascii.unhexlify(b))
# #             b = b[0]
#         chunklist[i].append(b)
# #
#         byte = f.read(4)
# f.close()

#
#
# print(chunklist)
# CHECKS FOR DUPLICATES
# coords = []
# for num in range(700):
#     coord = [chunklist[0][num], chunklist[1][num]]
#     coords.append(coord)
# print(coords)
# i = 0
# for acoord in coords:
#     print(acoord)
#     repeats = (coords.count(acoord))
#     print(repeats)
#     if repeats > 1 and acoord != [b'00000000', b'00000000']:
#         print("eureka")
#         print(i)
#         break
#     i += 1


# print(chunklist[2].index(b'7c79ea01'))
# print(chunklist[2].index(b'7cbafa01'))
# print(chunklist[0][434], chunklist[1][434])
# print(chunklist[2].count(b'7c79ea01'))
