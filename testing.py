## THIS IS UGLY CODE

# NUMBER CONVERSIONS
def hex2dec(num):
    """
    convert a hex value in base 16 to an int
    :param num: a hex value in string format
    :return: converted value
    """
    dec = int(num, base=16)

    return dec

test_values = ["10410", "c000c", "d041c"]
for i in range(len(test_values)):
    print("hex value", test_values[i], "as < class int > ", hex2dec(test_values[i]))

remainder = hex2dec(test_values[1]) % hex2dec(test_values[0])
print("remainder of offset / chunk as int:", remainder)
print("remainder formatted as hex: {:X}".format(remainder))
print('----------------------------------------------------------------')


# DATA VALIDATION
import string  # why is this error occurring?  it is used below


def char_itr_string_digits(strng):
    """
    *** See function char_in_string_hex_digits for a better function***
    Check if every character in a string is present in string.digits
    by taking each char and iterating through string.digits
    :param strng:
    :return: found as boolean value
    """
    idx = 0
    i = 0
    found = 0

    while i < len(strng):
        while idx < len(string.digits):
            if strng[i] == string.digits[idx]:
                found += 1
                idx = len(string.digits)
            else:
                idx += 1
        i += 1
        idx = 0

    if found == len(strng):
        found = True
    else:
        found = False

    return found

my_string = "1c"
print("Are all characters in", my_string, "in string.digits?")
print(char_itr_string_digits(my_string))
print('----------------------------------------------------------------')

# HEX STRING DIGITS
import string


def print_hex():
    for i in range(len(string.hexdigits)):
        print(string.hexdigits[i], end="")
    print("")

print_hex()
print('----------------------------------------------------------------')


def char_in_string_hex_digits(strng):
    i = 0
    found = 0

    while i < len(strng):
        if strng[i] in string.hexdigits:
            found += 1
        i += 1

    if found == len(strng):
        found = True
    else:
        found = False

    return found

s = "12345a"
print("Are all characters in", s, "in string.hexdigits?")
print(char_in_string_hex_digits(s))
print('----------------------------------------------------------------')


import struct
import binascii


def hex2bin(hexstr):
    """
    Return the binary data represented by the hexadecimal string
    :param hexstr: hexadecimal string to be converted
    :return: binary data
    """
    binnum = (binascii.unhexlify(hexstr))

    return binnum


def unpack_binary(binnum, fmt='<L'):
    """
    Unpack from the buffer (presumably packed by pack(fmt, ...)) according to the format string fmt)
    Output is a tuple
    :param binnum: binary number to unpack
    :param fmt: format for unpacking.  < = little endian.  > = big endian.  L = unsigned long
    :return: tuple[0], so int
    """

    newint = struct.unpack(fmt, binnum)[0]

    return newint


def pack_to_binary(num, fmt='<I'):
    """
    Return a string (usually binary in this use case) containing the values v, v2 packed according to the given format
    :param num: value to be packed
    :param fmt: format for packing.  < = little endian.  > = big endian.  I = unsigned integer
    :return: binary (other options?) value
    """
    newbin = (struct.pack(fmt, num))

    return newbin


def binary_calculator(binnum):
    a = (binascii.unhexlify('06010000'))
    print("a is", a)

    a1 = struct.pack("I", struct.unpack('<L', a)[0] + 1)
    print("a1 is", a1)
    print("a1 type is", type(a1))

    b = binascii.hexlify(a)
    print("b is", b)

    c = struct.unpack('<L', a1)
    print(c[0])
    print(hex(c[0]))



chunkstring = "06010000"
binary_data = (hex2bin(chunkstring))
unpacked_int = (unpack_binary(binary_data))
print("The binary value", binary_data, "unpacked, little endian, to int =", unpacked_int)
packed_int = pack_to_binary(unpacked_int)
print("The int", unpacked_int, "packed to little endian =", packed_int)
more()
'----------------------------------------------------------------------------------------------------------------------'

