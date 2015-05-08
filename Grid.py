# CODE IS CURRENTLY BUTT-UGLY!!

__author__ = 'lena'

from ChunkOffsets import get_input
import string
import turtle


def column(a, x, y):
    for idx in range(16):
        a = int(a, base=16) + 256
        a = hex(a)
        # a = b
        slim.goto(x, y)
        slim.write(a[2:], move=False, align="center", font=("Arial", 16, "bold"))
        y -= 20
    return a


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

for i in range(16):
    if i == 0:
        my_offset = c + 20
    else:
        my_offset = int(my_offset, base=16) + 256
    my_offset = hex(my_offset)
    # a = b
    slim.goto(0, y)
    slim.write(my_offset[2:], move=False, align="center", font=("Arial", 16, "bold"))
    y -= 20

for test in range(16):
    x += 150
    y = 320
    my_offset = column(my_offset, x, y)

wn.exitonclick()
