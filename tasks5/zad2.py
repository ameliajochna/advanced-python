import math
import turtle


def draw_rectangle(a: int, b: int, rotation: int, t: turtle.Turtle) -> None:
    t.left(rotation)
    t.forward(a)
    t.left(rotation)
    t.forward(b)
    t.left(rotation)
    t.forward(a)
    t.left(rotation)
    t.forward(b)


def draw_sinusoidal_wave(t: turtle.Turtle) -> None:
    for i in range(0, 360, 5):
        val = int(200 * math.sin(math.radians(i)))
        print(val)
        draw_rectangle(val, 5, 90, t)
        t.forward(5)


def main() -> None:
    turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)

    draw_sinusoidal_wave(t)


if __name__ == "__main__":
    main()
