import turtle

from tasks2.big_numbers import give_number


def draw_square(size):
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()


def draw_digit(digit, width):
    for row in digit:
        for _ in row:
            turtle.penup()
            turtle.forward(width / 5)
            turtle.pendown()
            if _ == "#":
                draw_square(width / 5)

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


def draw_mosaic():
    digit_to_draw = give_number(5)
    draw_digit(digit_to_draw, 100)


def main():
    turtle_obj = turtle.Turtle()
    screen = turtle.Screen()

    turtle_obj.penup()
    turtle_obj.goto(-300, 250)
    turtle_obj.pendown()

    draw_mosaic(turtle_obj)

    screen.mainloop()


if __name__ == "__main__":
    main()
