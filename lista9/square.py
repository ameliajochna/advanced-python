#################################################
# kwadrat.py
#################################################

from turtle import (
    begin_fill,
    end_fill,
    fd,
    fillcolor,
    goto,
    pd,
    pu,
    rt,
    speed,
    tracer,
)

BOK = 15
SX = -100
SY = 0


def kwadrat(x, y, kolor):
    fillcolor(kolor)
    pu()
    goto(SX + x * BOK, SY + y * BOK)
    pd()
    begin_fill()
    for i in range(4):
        fd(BOK)
        rt(90)
    end_fill()


def main():
    tracer(0, 1)
    speed('fastest')
    kolory = ['red', 'green', 'blue']

    for i in range(10):
        kwadrat(i, i, kolory[i % 3])

    input()


if __name__ == '__main__':
    main()
