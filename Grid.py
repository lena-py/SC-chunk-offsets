# CODE IS CURRENTLY BUTT-UGLY!!

__author__ = 'lena'

from ChunkOffsets import get_input

import string


c = get_input(input("Enter an offset (first is 'c000c')\n"), string.hexdigits,
              "Not a valid hex chunk number.  Try again.\n")

import turtle
slim = turtle.Turtle()
wn = turtle.Screen()
wn.setworldcoordinates(-20, -20, 1960, 320)
slim.speed(0)
x = 0

a = c + 20
a = hex(a)
# a = b
slim.hideturtle()
slim.penup()
slim.goto(0, 320)
slim.write(a[2:], move=False, align="center", font=("Arial", 16, "bold"))
y = 300


for i in range(15):
    a = int(a, base=16) + 256
    a = hex(a)
    # a = b
    slim.goto(0, y)
    slim.write(a[2:], move=False, align="center", font=("Arial", 16, "bold"))
    y -= 20

# x = 50
# y = 320


def column(a, x, y):
    for idx in range(16):
        a = int(a, base=16) + 256
        a = hex(a)
        # a = b
        slim.goto(x, y)
        slim.write(a[2:], move=False, align="center", font=("Arial", 16, "bold"))
        y -= 20
    return a

for test in range(15):
    x += 150
    y = 320
    a = column(a, x, y)
    #column(a, x, y)
    #a = int(a, base=16) + 256



# column(a, b, x, y)



wn.exitonclick()
