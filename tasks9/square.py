import turtle

SIDE_LENGTH = 15
SX = -100
SY = 0


def square(x: int, y: int, colour: str) -> None:
    turtle.fillcolor(colour)
    turtle.pu()
    turtle.goto(SX + x * SIDE_LENGTH, SY + y * SIDE_LENGTH)
    turtle.pd()
    turtle.begin_fill()
    for i in range(4):
        turtle.fd(SIDE_LENGTH)
        turtle.rt(90)
    turtle.end_fill()


def main() -> None:
    turtle.tracer(0, 1)
    turtle.speed("fastest")
    colours = ["red", "green", "blue"]

    for i in range(10):
        square(i, i, colours[i % 3])

    input()


if __name__ == "__main__":
    main()
