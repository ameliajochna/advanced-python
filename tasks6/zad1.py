import turtle

from tasks2.big_numbers import give_number


def draw_square(size: int) -> None:
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()


def draw_digit(digit: list, width: int) -> None:
    for row in digit:
        for _ in row:
            turtle.penup()
            turtle.forward(width / 5)
            turtle.pendown()
            if _ == "#":
                draw_square(width // 5)

        turtle.penup()
        turtle.backward(width)
        turtle.right(90)
        turtle.forward(width / 5)
        turtle.left(90)
        turtle.pendown()

    turtle.penup()
    turtle.left(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(int(6 / 5 * width))
    turtle.penup()


def draw_mosaic() -> None:
    digit_to_draw = give_number(5)
    draw_digit(digit_to_draw, 100)


def main() -> None:
    turtle_obj = turtle.Turtle()
    screen = turtle.Screen()

    turtle_obj.penup()
    turtle_obj.goto(-300, 250)
    turtle_obj.pendown()

    draw_mosaic()

    screen.mainloop()


if __name__ == "__main__":
    main()
