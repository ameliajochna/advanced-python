import math
import turtle


def rectangle(a, b, rotation, t):
    t.left(rotation)
    t.forward(a)
    t.left(rotation)
    t.forward(b)
    t.left(rotation)
    t.forward(a)
    t.left(rotation)
    t.forward(b)


def sinus(t):
    for i in range(0, 360, 5):
        val = int(200 * math.sin(math.radians(i)))
        print(val)
        rectangle(val, 5, 90, t)
        t.forward(5)


def main():
    t = turtle.Turtle()
    screen = turtle.Screen()
    t.speed(0)

    sinus(t)

    screen.mainloop()


if __name__ == "__main__":
    main()
