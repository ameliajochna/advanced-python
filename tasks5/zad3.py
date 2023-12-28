import random
import turtle

from tasks2.big_numbers import give_number


def draw_square(size: int, t: turtle.Turtle) -> None:
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()


def draw_number(number: list, width: int, t: turtle.Turtle) -> None:
    for i in range(len(number)):
        for j in range(len(number[i])):
            t.penup()
            t.forward(width / 5)
            t.pendown()
            if number[i][j] == "#":
                draw_square(width // 5, t)

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


def draw_numbers(numbers_str: str, t: turtle.Turtle) -> None:
    numbers = [int(num) for num in numbers_str]

    for i in range(len(numbers)):
        t.fillcolor(random.random(), random.random(), random.random())
        draw_number(give_number(numbers[i]), 100, t)


def main() -> None:
    turtle.Screen()

    t = turtle.Turtle()
    t.penup()
    t.goto(-300, 250)
    t.pendown()
    numbers_str = "2560"
    draw_numbers(numbers_str, t)


if __name__ == "__main__":
    main()
