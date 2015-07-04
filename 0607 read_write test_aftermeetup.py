__author__ = 'lena'
import binascii
import struct
import os

# __file__ is a dunder to designate where it is
# wrap the code in a function and then pass the path to the function
# os.path.dirname will return the directory of a file
# use list comprehension to be sure you get files with just .dat
# unit tests in nose
# file.stat to find the size of the file
# from collections import counter to maintain a separate counter
# two scoops of django
# anaconda (notebooks, pandas)
# iterm2 instead of terminal
# homebrew
# hitchkiker's guide to python
#
"""
look in the file module for seek
"""


def template_dictionary(path):
    templates = {}
    for root, dirs, files in os.walk(path):
        all_files = [file for file in files if ".dat" in file]

    for i in range(len(all_files)):
        file = all_files[i]
        with open(path + file, "rb") as f:
            hexed_file = binascii.hexlify(f.read())
            body = hexed_file[:131072]
            surface_points = hexed_file[131072:]
            templates[file] = [body, surface_points]
    return templates

chunk_templates = template_dictionary("/Users/lena/PycharmProjects/SC-chunk-offsets2/chunk_templates/")
print((chunk_templates['Chunk2.dat'][0][:50]))
print(list(chunk_templates.keys()))

outfile = open("Chunk_out.dat", "wb")


with open("chunks.dat", "rb") as f:
    # Read the complete directory of chunks
    directory = f.read(786444)

    # Create a list of chunks
    all_chunks = []
    current_chunk = binascii.hexlify(f.read(66576))

    for num in range(1000):
        header = current_chunk[:32]
        blocks = current_chunk[32:131072]
        surface_points = current_chunk[131072:133152]
        one_chunk = [[]]
        x_coord = header[16:24]
        z_coord = header[24:32]
        one_chunk[0].append(x_coord)
        one_chunk[0].append(z_coord)
        one_chunk.append(blocks)
        one_chunk.append(surface_points)
        all_chunks.append(one_chunk)
        current_chunk = binascii.hexlify(f.read(66576))

    count = 0
    for i in range(len(all_chunks)):
        chunk_body = all_chunks[i][1]
        chunk_surface_points = all_chunks[i][2]
        if chunk_body.count(b'44004400440044004400440044004400') > 0:
            count += 1
            all_chunks[i][1] = chunk_templates['chunk8'][0]
            all_chunks[i][2] = chunk_templates['chunk8'][1]
        elif chunk_body.count(b'4400440044004400440044004400') > 0:
            count += 1
            all_chunks[i][1] = chunk_templates['chunk7'][0]
            all_chunks[i][2] = chunk_templates['chunk7'][1]
        elif chunk_body.count(b'440044004400440044004400') > 0:
            count += 1
            all_chunks[i][1] = chunk_templates['chunk6'][0]
            all_chunks[i][2] = chunk_templates['chunk6'][1]
        elif chunk_body.count(b'44004400440044004400') > 0:
            count += 1
            all_chunks[i][1] = chunk_templates['chunk5'][0]
            all_chunks[i][2] = chunk_templates['chunk5'][1]
        elif chunk_body.count(b'4400440044004400') > 0:
            count += 1
            all_chunks[i][1] = chunk_templates['chunk4'][0]
            all_chunks[i][2] = chunk_templates['chunk4'][1]
        elif chunk_body.count(b'440044004400') > 0:
            count += 1
            all_chunks[i][1] = chunk_templates['chunk3'][0]
            all_chunks[i][2] = chunk_templates['chunk3'][1]
        elif chunk_body.count(b'44004400') > 0:
            count += 1
            all_chunks[i][1] = chunk_templates['chunk2'][0]
            all_chunks[i][2] = chunk_templates['chunk2'][1]

    bytes_again = b''
    for i in range((1000)):
        bytes_again += b'efbeaddeffffffff'
        bytes_again += all_chunks[i][0][0]
        bytes_again += all_chunks[i][0][1]
        bytes_again += all_chunks[i][1]
        bytes_again += all_chunks[i][2]

        # print(bytes_again)
    bytes_again = binascii.unhexlify(bytes_again)

    print(type(all_chunks[0][0][0]))
    print(count)
    outfile.write(directory)
    outfile.write(bytes_again)
    outfile.close()
    f.close()

    print("done")



