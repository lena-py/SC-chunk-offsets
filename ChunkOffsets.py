__author__ = 'lena'
import string


def check_iterations(any_iterations):
    idx = 0
    found = False
    while idx < 10 and not found:
        if any_iterations[0] == string.digits[idx]:
            found = True
            return found
        else:
            idx += 1
    return found


def next_offset(any_offset):
    add_on = int("10410", base=16)
    new_offset = (any_offset + add_on)

    return new_offset


def print_offset(any_offset, any_iterations):

    print("OFFSETS\n------")
    print(hex(any_offset), "\n------")

    for i in range(any_iterations):
        any_offset = next_offset(any_offset)
        print(hex(any_offset))
        print("-------")


def main():

    hex_chunk = int("10410", base=16)
    my_offset = int(input("Enter an offset (first is 'c000c')\n"), base=16)
    # 54108 is the calculated remainder (base 10) of a valid chunk // 10410
    while my_offset % hex_chunk != 54108:
        my_offset = int(input("Enter a valid chunk offset number please\n"), base=16)

    my_iterations = input("How many offsets to generate? 1 - oo\n")
    while not check_iterations(my_iterations):
        my_iterations = input("You must enter a number\n")
        check_iterations(my_iterations)

    my_iterations = int(my_iterations)

    print_offset(my_offset, my_iterations)
    print("this is a test")


if __name__ == "__main__":
    main()