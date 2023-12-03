import math
import turtle

t = turtle.Turtle()
screen = turtle.Screen()


def rectangle(a, b, rotation):
    t.left(rotation)
    t.forward(a)
    t.left(rotation)
    t.forward(b)
    t.left(rotation)
    t.forward(a)
    t.left(rotation)
    t.forward(b)


def sinus():
    for i in range(0, 360, 5):
        val = int(200 * math.sin(math.radians(i)))
        print(val)
        rectangle(val, 5, 90)
        t.forward(5)


t.speed(0)

sinus()

screen.mainloop()
