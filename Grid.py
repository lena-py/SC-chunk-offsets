__author__ = 'lena'

from ChunkOffsets import get_input
import string
import turtle


def table(oa, ox, oy):
    for test in range(16):
        # print(test)
        # print("after call a is type", type(a))
        for idx in range(16):
            if idx == 0 and test == 0:
                oa = oa
            else:
                oa = int(oa, base=16) + 256
                oa = hex(oa)
            slim.goto(ox, oy)
            slim.write(oa[2:], move=False, align="center", font=("Arial", 16, "bold"))
            oy -= 20
            # print("slim wrote idx", idx)
        # print("round", test)
        ox += 150
        oy = 320


# def main():
c = get_input(input("Enter an offset (first is 'c000c')\n"), string.hexdigits,
              "Not a valid hex chunk number.  Try again.\n")
my_offset = c + 20
my_offset = hex(my_offset)
y = 320
x = 0

slim = turtle.Turtle()
wn = turtle.Screen()
wn.setworldcoordinates(-20, -20, 1960, 320)
slim.speed(0)
slim.hideturtle()
slim.penup()
slim.goto(x, y)

# print("before function call my_offset is", type(my_offset))
table(my_offset, x, y)

wn.exitonclick()

# main()
