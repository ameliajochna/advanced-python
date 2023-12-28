import turtle


def rhomb(a, b, angle, t):
    t.left(angle)
    t.forward(a)
    t.left(180 - angle)
    t.forward(b)
    t.left(angle)
    t.forward(a)
    t.left(180 - angle)
    t.forward(b)


def flower(N, t):
    for _ in range(N):
        rhomb(50, 50, 150, t)
        t.right(360 / N)


def bouquet(n, t):
    t.left(90)
    n = str(n)
    N = len(str(n))
    for i in range(N):
        c = n[i]
        t.forward(200)

        if i == 0:
            t.pencolor("red")

        flower(int(c) + 3, t)

        t.pencolor("black")

        t.backward(200)
        t.rt(360 / N)


def main():
    t = turtle.Turtle()
    screen = turtle.Screen()

    t.setposition(0, 0)
    t.speed(0)

    bouquet("59257", t)

    screen.mainloop()


if __name__ == "__main__":
    main()
