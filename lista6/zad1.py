import turtle

from duze_cyfry import daj_cyfre

t = turtle.Turtle()
screen = turtle.Screen()


def kwadrat(size):
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()


def rysuj_liczbe(cyfra, width):
    for i in range(len(cyfra)):
        for j in range(len(cyfra[i])):
            t.penup()
            t.forward(width / 5)
            t.pendown()
            if cyfra[i][j] == '#':
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


def mozaika():
    rysuj_liczbe(daj_cyfre(5), 100)


t.penup()
t.goto(-300, 250)
t.pendown()

screen.mainloop()
