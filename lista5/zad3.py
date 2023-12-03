import random
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


def rysuj_liczbe(liczba, width):
    for i in range(len(liczba)):
        for j in range(len(liczba[i])):
            t.penup()
            t.forward(width / 5)
            t.pendown()
            if liczba[i][j] == '#':
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


def wyznacz_liczby(liczby_str):
    liczby = []
    for l in liczby_str:
        liczby.append(int(l))

    for i in range(len(liczby)):
        t.fillcolor(random.random(), random.random(), random.random())
        rysuj_liczbe(daj_cyfre(liczby[i]), 100)


t.penup()
t.goto(-300, 250)
t.pendown()

liczba = '2560'
wyznacz_liczby(liczba)


screen.mainloop()
