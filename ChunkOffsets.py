__author__ = 'lena'
import string
_CHUNK_LENGTH = int("10410", base=16)


def valid_entry(entry, digits=string.digits):
    # scaffolding code print(len(entry))
    idx = 0
    i = 0
    found = 0

    while i < len(entry):
        while idx < len(digits):
            # scaffolding code print("idx", idx, "i", i)
            if entry[i] == digits[idx]:
                found += 1
                # scaffolding code print("found")
                idx = len(digits)
            else:
                idx += 1
                # scaffolding code print("not found")
        i += 1
        idx = 0
        # scaffolding code print("round")

    # scaffolding code print(found)

    if found == len(entry):
        if digits == string.hexdigits:
            if int(entry, base=16) % _CHUNK_LENGTH == 54108:
                found = True
            else:
                # scaffolding code print("not a valid hex number shit head")
                found = False
    else:
        found = False
    return found


def next_offset(offset):
    new_offset = (offset + _CHUNK_LENGTH)

    return new_offset


def print_offset(offset, itr):

    print("OFFSETS\n------")
    print(hex(offset), "\n------")

    for i in range(itr):
        offset = next_offset(offset)
        print(hex(offset))
        print("-------")


def main():

    my_offset = input("Enter an offset (first is 'c000c')\n")
    while not valid_entry(my_offset, string.hexdigits):
        my_offset = input("Not a valid chunk hex offset.  Try again.\n")
        valid_entry(my_offset, string.hexdigits)

    my_iterations = input("How many offsets to generate? 1 - oo\n")
    while not valid_entry(my_iterations):
        my_iterations = input("You must enter a number\n")
        valid_entry(my_iterations)

    my_offset = int(my_offset, base=16)
    my_iterations = int(my_iterations)
    print_offset(my_offset, my_iterations)

if __name__ == "__main__":
    main()