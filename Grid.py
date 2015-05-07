# CODE IS CURRENTLY BUTT-UGLY!!

__author__ = 'lena'

from ChunkOffsets import get_input

import string


c = get_input(input("Enter an offset (first is 'c000c')\n"), string.hexdigits,
              "Not a valid hex chunk number.  Try again.\n")

import turtle
slim = turtle.Turtle()
wn = turtle.Screen()
wn.setworldcoordinates(-20, -20, 320, 320)
slim.speed(0)

a = (c) + 20
b = hex(a)
a = b
slim.hideturtle()
slim.penup()
slim.goto(0, 320)
slim.write(b[2:], move=False, align="center", font=("Arial", 16, "bold"))
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
        # return a,b,x,y
for test in range(5):
    column(a, b, x, y)
    #a = int(a, base=16) + 256

    x += 50
    y = 320

# column(a, b, x, y)



wn.exitonclick()
