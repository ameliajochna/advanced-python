import random
import turtle

SQUARE_WIDTH = 50


def square(a: int, color: tuple, t: turtle.Turtle) -> None:
    t.pencolor(int(color[0]), int(color[1]), int(color[2]))
    t.fillcolor(int(color[0]), int(color[1]), int(color[2]))
    t.begin_fill()
    for _ in range(4):
        t.forward(a)
        t.left(90)
    t.end_fill()


def randomize(content: str) -> list:
    cnt = content.count("\n") + 1
    content_arr = content.replace("\n", " ").split(" ")
    row_len = int(len(content_arr) / cnt)
    random.shuffle(content_arr)
    cur_len = 0
    cur_row = ""
    ans = []
    for t in content_arr:
        if cur_len == row_len:
            ans += [[cur_row]]
            cur_len = 0
            cur_row = ""

        cur_row += t
        cur_len += 1
        if cur_len != 3:
            cur_row += " "
    ans += [[cur_row]]
    return ans


def read_file(path: str, t: turtle.Turtle) -> None:
    with open(path) as file:
        content = randomize(file.read())
        for line in content:
            arr = line[0].split(" ")
            for w in arr:
                square(SQUARE_WIDTH, eval(w), t)
                t.forward(SQUARE_WIDTH)

            t.penup()
            t.backward(SQUARE_WIDTH * len(arr))
            t.right(90)
            t.forward(SQUARE_WIDTH)
            t.left(90)
            t.pendown()


def main() -> None:
    t = turtle.Turtle()
    screen = turtle.Screen()

    screen.tracer(0, 1)

    screen.colormode(255)

    read_file("img1.txt", t)

    screen.mainloop()


if __name__ == "__main__":
    main()
