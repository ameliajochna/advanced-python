import turtle

t = turtle.Turtle()
screen = turtle.Screen()


def romb(a, b, angle):
    t.left(angle)
    t.forward(a)
    t.left(180 - angle)
    t.forward(b)
    t.left(angle)
    t.forward(a)
    t.left(180 - angle)
    t.forward(b)


def flower(N):
    for _ in range(N):
        romb(50, 50, 150)
        t.right(360 / N)


def bukiet(n):
    t.left(90)
    n = str(n)
    N = len(str(n))
    for i in range(N):
        c = n[i]
        t.forward(200)

        if i == 0:
            t.pencolor('red')

        flower(int(c) + 3)

        t.pencolor('black')

        t.backward(200)
        t.rt(360 / N)


t.setposition(0, 0)
t.speed(0)


bukiet('59257')


screen.mainloop()
