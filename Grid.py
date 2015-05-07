__author__ = 'lena'

import turtle
slim = turtle.Turtle()
wn = turtle.Screen()
wn.setworldcoordinates(-20, -20, 320, 320)
slim.speed(0)

c = "d041c"
print(c)
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

for i in range(16):
    a = int(a, base=16) + 256
    b = hex(a)
    a = b
    slim.goto(x, y)
    slim.write(b[2:], move=False, align="center", font=("Arial", 16, "bold"))
    y -= 20

x = 100
y = 320

for i in range(16):
    a = int(a, base=16) + 256
    b = hex(a)
    a = b
    slim.goto(x, y)
    slim.write(b[2:], move=False, align="center", font=("Arial", 16, "bold"))
    y -= 20

wn.exitonclick()
