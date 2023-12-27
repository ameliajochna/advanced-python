import turtle

from lista6.big_numbers import give_number


def kwadrat(size, t):
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()


def rysuj_liczbe(cyfra, width, t):
    for i in range(len(cyfra)):
        for j in range(len(cyfra[i])):
            t.penup()
            t.forward(width / 5)
            t.pendown()
            if cyfra[i][j] == "#":
                kwadrat(width / 5)

        t.penup()
        t.backward(width)
        t.right(90)
        t.forward(width / 5)
        t.left(90)
        t.pendown()
    t.penup()
    t.left(90)
    t.forward(width)
    t.right(90)
    t.forward(int(6 / 5 * width))
    t.penup()


def mozaika(t):
    rysuj_liczbe(give_number(5), 100, t)


def main():
    t = turtle.Turtle()
    screen = turtle.Screen()

    t.penup()
    t.goto(-300, 250)
    t.pendown()

    mozaika(t)

    screen.mainloop()


if __name__ == "__main__":
    main()
