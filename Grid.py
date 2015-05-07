# CODE IS CURRENTLY BUTT-UGLY!!

__author__ = 'lena'
from ChunkOffsets import valid_entry
import string

c = input("Enter an offset (first is 'c000c')\n")
while not valid_entry(c, string.hexdigits):
    my_offset = input("Not a valid chunk hex offset.  Try again.\n")
    valid_entry(my_offset, string.hexdigits)

import turtle
slim = turtle.Turtle()
wn = turtle.Screen()
wn.setworldcoordinates(-20, -20, 320, 320)
slim.speed(0)

a = hex(int(c, base=16) + 20)
slim.hideturtle()
slim.penup()
slim.goto(0, 320)
slim.write(a[2:], move=False, align="center", font=("Arial", 16, "bold"))
y = 300


for i in range(15):
    a = int(a, base=16) + 256
    b = hex(a)
    a = b
    slim.goto(0, y)
    slim.write(b[2:], move=False, align="center", font=("Arial", 16, "bold"))
    y -= 20

x = 50
y = 320


def column(a, b, x, y):
    for idx in range(16):
        a = int(a, base=16) + 256
        b = hex(a)
        a = b
        slim.goto(x, y)
        slim.write(b[2:], move=False, align="center", font=("Arial", 16, "bold"))
        y -= 20

column(a, b, x, y)

x = 100
y = 320

column(a, b, x, y)

# for i in range(16):
#     a = int(a, base=16) + 256
#     b = hex(a)
#     a = b
#     slim.goto(x, y)
#     slim.write(b[2:], move=False, align="center", font=("Arial", 16, "bold"))
#     y -= 20

wn.exitonclick()
