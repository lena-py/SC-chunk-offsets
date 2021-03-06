__author__ = 'lena'
import binascii
import struct
from ChunkOffsets import create_offset_list

generated_offsets = create_offset_list(786444, 700)


with open("chunks.dat", "rb") as f:
    # Read the complete chunk directory
    complete_directory_of_chunks = f.read(786444)
    # Create a list of the 12 byte header entries
    directory_array = []
    idx1 = 0
    idx2 = 12
    for i in range(700):
        one_header = binascii.hexlify(complete_directory_of_chunks[idx1:idx2])
        directory_array.append(one_header)
        idx1 = idx2
        idx2 += 12
    #print(directory_array)

    # Separate the 12 byte header entries into 8 byte coordinates and 4 byte offset
    directory_array_final = []
    offsets = []
    for i in range(len(directory_array)):
        xzo = [[]]

        x = directory_array[i][:8]
        z = directory_array[i][8:16]
        o = struct.unpack('<L', binascii.unhexlify(directory_array[i][16:]))
        o = o[0]
        xzo[0].append(x)
        xzo[0].append(z)
        offsets.append(o)
        directory_array_final.append(xzo)

    print(directory_array_final)
    print("OFFSETS", offsets)




    # Create an array of coordinates as recorded in the chunk bodies
    chunk_body_coords_final = []
    one_chunk = binascii.hexlify(f.read(66576))
    for num in range(700):
        header = one_chunk[:32]
        xz = [[]]
        x = header[16:24]
        z = header[24:32]
        xz[0].append(x)
        xz[0].append(z)
        chunk_body_coords_final.append(xz)
        one_chunk = binascii.hexlify(f.read(66576))
    print(chunk_body_coords_final)

    count = 0
    for i in range(600):
        if chunk_body_coords_final[i] != directory_array_final[i] and chunk_body_coords_final[i] != [[b'', b'']]:
            print("i = ", i, "directory = ", directory_array_final[i], "chunk body = ", chunk_body_coords_final[i])
            count += 1
    print(count)

    count = 0
    for i in range(700):
        if generated_offsets[i] != offsets[i] and offsets[i] != 0:
            count += 1
            print(hex(generated_offsets[i]), hex(offsets[i]))
    print(count)

    # Find repeated chunks by coordinates in the body
    # how_many = 0
    # counter = 0
    # for a_coord in chunk_body_coords_final:
    #     repeats = chunk_body_coords_final.count(a_coord)
    #     if repeats > 1 and a_coord != b'' and a_coord != b'\x00\x00\x00\x00\x00\x00\x00\x00':
    #         how_many += 1
    #         print(counter, binascii.hexlify(a_coord))
    #     counter += 1
    #
    # print(how_many)
    #
    # f.close()

# Create coordinates from chunk directory
#
# with open("chunks.dat", "rb") as f:
#     byte = f.read(4)
#     chunklist = [[], [], []]
#     print(byte)
#     for num in range(630):
#         for i in range(3):
#             b = binascii.hexlify(byte)
#
#             # print(struct.unpack('<L', binascii.unhexlify(b)))
#             b = struct.unpack('<L', binascii.unhexlify(b))
#             b = b[0]
#             chunklist[i].append(b)
#
#             byte = f.read(4)
#
#
# print(chunklist)
# dir_coords = []
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

