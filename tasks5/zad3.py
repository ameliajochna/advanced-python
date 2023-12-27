import random
import turtle

from lista5.big_numbers import give_number


def kwadrat(size, t):
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()


def rysuj_liczbe(liczba, width, t):
    for i in range(len(liczba)):
        for j in range(len(liczba[i])):
            t.penup()
            t.forward(width / 5)
            t.pendown()
            if liczba[i][j] == "#":
                kwadrat(width / 5, t)

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


def wyznacz_liczby(liczby_str, t):
    liczby = []
    for num in liczby_str:
        liczby.append(int(num))

    for i in range(len(liczby)):
        t.fillcolor(random.random(), random.random(), random.random())
        rysuj_liczbe(give_number(liczby[i]), 100, t)


def main():
    t = turtle.Turtle()
    screen = turtle.Screen()

    t.penup()
    t.goto(-300, 250)
    t.pendown()

    liczba = "2560"
    wyznacz_liczby(liczba, t)

    screen.mainloop()


if __name__ == "__main__":
    main()
