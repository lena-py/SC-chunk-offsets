__author__ = 'lena'
import binascii
import struct
import os
import datetime

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
    """ Return a dictionary of template files.

    Args:
        path(str): The OS path to the directory containing the templates

    Returns:
        templates(dict): Keys are file names and values are lists of chunk body and surface points
    """
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


def search_replace(achunk, templates, multiplier=14):
    """ Search for a conversion code and replace with an item from the dictionary if found.

    Args:
        achunk(bytes): an entire single chunk
        multiplier(int): the maximum chunk conversion code number

    Returns:
        achunk(bytes): if no conversion code is found then return original achunk.
            Otherwise, return the convertered achunk
    """
    count = 0
    header = achunk[:32]
    blocks = achunk[32:131072]
    # surface_points = achunk[131072:133152]  Not needed but I might want it later
    for i in range(14):
            value = b'4400' * multiplier
            if value in blocks and multiplier != 1:
                print("MULT IS:", multiplier)
                key = "Chunk{}.dat".format(multiplier)
                blocks = templates[key][0]
                surface_points = templates[key][1]
                achunk = header + blocks + surface_points
                break
            multiplier -= 1
    return achunk


def main():
    start_time = datetime.datetime.now()
    chunk_templates = template_dictionary("/Users/lena/PycharmProjects/SC-chunk-offsets2/chunk_templates/")

    with open("Chunk_out.dat", "wb") as outfile:
        with open("chunks.dat", "rb") as f:
            # Read the complete directory of chunks
            directory = f.read(786444)
            outfile.write(directory)

            current_chunk = binascii.hexlify(f.read(66576))
            for num in range(2000):
                current_chunk = search_replace(current_chunk, chunk_templates)
                outfile.write(binascii.unhexlify(current_chunk))
                current_chunk = binascii.hexlify(f.read(66576))

        print("done")
    print(datetime.datetime.now() - start_time)
if __name__ == '__main__':
    main()
