__author__ = 'lena'


def next_offset(any_offset):
    addOn = int("10410", base=16)

    newOffset = (any_offset + addOn)

    return newOffset


def print_offset(anyOffset, anyIterations):

    print("OFFSETS\n------")
    print(hex(anyOffset), "\n------")

    for i in range(anyIterations):
        anyOffset = next_offset(anyOffset)
        print(hex(anyOffset))
        print("-------")


def main():

    myOffset = int(input("Enter an offset (first is 'c000c')\n"), base=16)
    myIterations = int(input("How many offsets to generate?\n"))

    print_offset(myOffset, myIterations)
    print("this is a test")


if __name__ == "__main__":
    main()