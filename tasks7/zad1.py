import turtle

SQUARE_WIDTH = 10


def square(a, color, t):
    t.pencolor(int(color[0]), int(color[1]), int(color[2]))
    t.color(int(color[0]), int(color[1]), int(color[2]))
    t.begin_fill()
    for _ in range(4):
        t.forward(a)
        t.left(90)
    t.end_fill()


def read_file(path, t):
    f = open(path)
    content = f.read().split("\n")
    for line in content:
        arr = line.split(" ")
        for w in arr:
            square(SQUARE_WIDTH, eval(w), t)
            t.forward(SQUARE_WIDTH)

        t.penup()
        t.backward(SQUARE_WIDTH * len(arr))
        t.right(90)
        t.forward(SQUARE_WIDTH)
        t.left(90)
        t.pendown()


def main():
    t = turtle.Turtle()
    screen = turtle.Screen()
    t.penup()
    t.goto(-300, 250)
    t.pendown()

    screen.tracer(0, 1)

    screen.colormode(255)

    read_file("img2.txt")

    t.penup()

    screen.mainloop()


if __name__ == "__main__":
    main()
