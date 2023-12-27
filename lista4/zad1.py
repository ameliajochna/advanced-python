import random
import turtle

SQUARE_SIZE = 5
ROWS = 80
COLUMNS = 80


def square(size, t):
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


def draw_board(t):
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

            square(SQUARE_SIZE, t)

            t.penup()
            t.forward(SQUARE_SIZE)
            t.pendown()

        t.penup()
        t.backward(SQUARE_SIZE * COLUMNS)
        t.right(90)
        t.forward(SQUARE_SIZE)
        t.left(90)
        t.pendown()


def main():
    t = turtle.Turtle()
    screen = turtle.Screen()

    screen.tracer(0, 0)

    t.speed(0)

    t.penup()
    t.goto(-300, 250)
    t.pendown()

    draw_board()

    screen.mainloop()


if __name__ == '__main__':
    main()
