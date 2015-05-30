__author__ = 'lena'
import string
_CHUNK_LENGTH = int("10410", base=16)


def get_input(entry, digits, message):
    while not valid_entry(entry, digits):
        entry = input(message)
        valid_entry(entry, digits)
    return int(entry, base=16)


def valid_entry(entry, digits=string.digits):
    i = 0
    found = 0

    if entry == "" or entry == "0":
        return found

    while i < len(entry):
        if entry[i] in digits:
            found += 1
        i += 1

    if found == len(entry):
        if digits == string.hexdigits:
            if int(entry, base=16) % _CHUNK_LENGTH == 54108:
                found = True
            else:
                found = False
    else:
        found = False

    return found


def next_offset(offset):
    new_offset = (offset + _CHUNK_LENGTH)
    return new_offset


def print_offset(offset, itr):
    print("OFFSETS\n------")
    print("{:X}".format(offset), "This uses the hex format option")
    print(hex(offset), "\n------")
    for i in range(itr):
        offset = next_offset(offset)
        print(hex(offset))
        print("-------")


def main():
    my_offset = input("Enter an offset (first is 'c000c')\n")
    my_offset = get_input(my_offset, string.hexdigits, "Not a valid hex chunk number.  Try again.\n")
    my_iterations = input("How many offsets to generate? 1 - oo\n")
    my_iterations = get_input(my_iterations, string.digits, "You must enter a positive integer.  Try again.\n")

    print_offset(my_offset, my_iterations)

if __name__ == "__main__":
    main()