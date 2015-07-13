__author__ = 'lena'
import binascii
import os
import datetime
from collections import Counter


def template_dictionary():
    """ Return a dictionary of conversion templates.

    Args:
        path(str): The OS path to the directory containing the templates

    Returns:
        templates(dict): Keys are identifier blocks and values are replacement blocks
    """
    templates = {b'7e': b'00', b'44': b'01'}

    return templates


def search_replace(achunk, templates, acounter, multiplier=1):
    """ Search for a conversion code and replace with an item from the dictionary if found.

    Args:
        achunk(bytes): an entire single chunk
        templates(dict): a dictionary of template files
        counter(collections.Counter): keeps track of number of occurrences of replaced chunks
        multiplier(int): the maximum chunk conversion code number

    Returns:
        achunk(bytes): if no conversion code is found then return original achunk.
            Otherwise, return the convertered achunk
        counter(collections.Counter): counter of replaced chunks
    """
    b = b''
    location = 0
    header = achunk[:32]
    blocks = achunk[32:131072]
    surface_points = achunk[131072:133152]
    # for i in templates:
    #         for iters in range(blocks.count(i)):
    #             start = location
    #             # print("yes")
    #             location = (achunk.find(i, start))
    #             # print(location)
    #             b = b + achunk[start:location] + b'45'
    #             location += 2
    #         b = b + achunk[location:]
    #
    # achunk = header + b + surface_points
    print(len(achunk))
    return achunk, acounter


def create_chunks_file(original_file, new_file, templates, iterations, acounter):
    """ Create a new chunks_dat file with chunks replaced that match a predefined code.

    Args:
        original_file(str): existing chunks.dat file
        new_file(str): the file to be created
        templates: chunk templates
        iterations: number of chunks in existing file
        acounter: keeps track of replaced chunks

    Returns:
        acounter: complete record of all replaced chunks
    """
    with open(new_file, "wb") as outfile:
        with open(original_file, "rb") as f:

            # Read the complete directory of chunks
            directory = f.read(786444)
            outfile.write(directory)

            current_chunk = binascii.hexlify(f.read(66576))
            for num in range(iterations):
                results = search_replace(current_chunk, templates, acounter)
                current_chunk = results[0]
                acounter = results[1]

                outfile.write(binascii.unhexlify(current_chunk))
                current_chunk = binascii.hexlify(f.read(66576))

    return acounter


def number_of_chunks(afile):
    """ Determine the number of chunks in a file

    Args:
        afile(bytes): a chunks file

    Return:
        int(result) or 0(int): valid file returns # chunks, invalid file returns 0
    """
    total_bytes = os.stat(afile).st_size
    header_size = 786444
    chunk_size = 66576
    result = (total_bytes-header_size) / chunk_size
    if result == int(result):
        return int(result)
    else:
        return 0


def main():
    start_time = datetime.datetime.now()
    counter = Counter({})
    chunk_templates = template_dictionary()
    in_file = "Chunks.dat"
    out_file = "Chunks_out.dat"

    total_chunks = number_of_chunks(in_file)
    if total_chunks > 0:
        # Creates the outfile and assigns the counter to the variable
        chunks_tally = create_chunks_file(in_file, out_file, chunk_templates, total_chunks, counter)
        print("Total blocks replaced:")
        for i in chunks_tally:
            print(i, chunks_tally[i])
    else:
        print("You're file is effed up.  Nothing was done")

    print("Time taken: {}".format(datetime.datetime.now() - start_time))

    print(number_of_chunks(out_file))

    with open("Untitled1.dat", 'rb') as f:
        f = (binascii.hexlify(f.read()))
        print(f)
        test_templates = {b'7e': b'41', b'44': b'20'}
        b = b''
        location = 0
        for i in range(f.count(b'99')):
            start = location
            # print("yes")
            location = (f.find(b'ff', start))
            # print(location)
            b = b + f[start:location] + b'45'
            location += 2
        b = b + f[location:]
        print(b)
        print(len(b), len(f))


if __name__ == '__main__':
    main()
