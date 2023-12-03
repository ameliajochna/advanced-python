import random
import turtle

t = turtle.Turtle()
screen = turtle.Screen()


def kwadrat(size):
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()


def brightness(color, bright):
    r, g, b = color
    r = min(max(0, r + bright * 0.3), 1)
    g = min(max(0, g + bright * 0.3), 1)
    b = min(max(0, b + bright * 0.3), 1)
    return (r, g, b)


screen.tracer(0, 0)

t.speed(0)

t.penup()
t.goto(-300, 250)
t.pendown()

SQUARE_SIZE = 5
ROWS = 80
COLUMNS = 80
for c in range(COLUMNS):
    for r in range(ROWS):
        color = (random.random(), random.random(), random.random())
        if c // (COLUMNS / 4) % 2 == 1:
            if (r // (ROWS / 4)) % 2 == 1:
                t.fillcolor(brightness(color, 1))
            else:
                t.fillcolor(brightness(color, -1))
        else:
            if (r // (ROWS / 4)) % 2 == 0:
                t.fillcolor(brightness(color, 1))
            else:
                t.fillcolor(brightness(color, -1))

        kwadrat(SQUARE_SIZE)

        t.penup()
        t.forward(SQUARE_SIZE)
        t.pendown()

    t.penup()
    t.backward(SQUARE_SIZE * COLUMNS)
    t.right(90)
    t.forward(SQUARE_SIZE)
    t.left(90)
    t.pendown()


screen.mainloop()
