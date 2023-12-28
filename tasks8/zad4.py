import math
import random
import turtle

import numpy

COLOURS = ["green", (0.5, 1, 0), "yellow", "orange", "red", (0.5, 0, 0)]
MAP_SIZE = 100
SQUARE_WIDTH = 10


def square(a: int, color: str | tuple, t: turtle.Turtle) -> None:
    """Draw a colored square of side length 'a' using the turtle 't'."""
    t.pencolor(color)
    t.color(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(a)
        t.left(90)
    t.end_fill()


def generate_map() -> list:
    """Generate a random matrix representing the map."""
    matrix = [[0.0] * MAP_SIZE for _ in range(MAP_SIZE)]
    n = 200

    # Randomly set some cells to a high value (representing a high elevation)
    for _ in range(n):
        i = random.randint(0, MAP_SIZE - 1)
        j = random.randint(0, MAP_SIZE - 1)
        matrix[i][j] = 4

    # Simulate a diffusion process to smooth out the elevations
    for _ in range(1000000):
        i = random.randint(0, MAP_SIZE - 1)
        j = random.randint(0, MAP_SIZE - 1)

        neighbours = [matrix[i][j]]
        if i - 1 >= 0:
            neighbours += [matrix[i - 1][j]]
        if i + 1 < MAP_SIZE:
            neighbours += [matrix[i + 1][j]]
        if j - 1 >= 0:
            neighbours += [matrix[i][j - 1]]
        if j + 1 < MAP_SIZE:
            neighbours += [matrix[i][j + 1]]

        matrix[i][j] = numpy.average(neighbours)

    # Normalize the values to be between 0 and 1
    max_value = numpy.amax(matrix)
    for i in range(MAP_SIZE):
        for j in range(MAP_SIZE):
            matrix[i][j] = matrix[i][j] / max_value

    return matrix


def draw_map(matrix: list, t: turtle.Turtle) -> None:
    """Draw the map using the turtle 't'."""
    for i in range(MAP_SIZE):
        for j in range(MAP_SIZE):
            colour_id = math.floor(matrix[i][j] / 0.2)
            square(SQUARE_WIDTH, COLOURS[colour_id], t)
            t.forward(SQUARE_WIDTH)

        t.penup()
        t.backward(SQUARE_WIDTH * MAP_SIZE)
        t.right(90)
        t.forward(SQUARE_WIDTH)
        t.left(90)
        t.pendown()


def main() -> None:
    t = turtle.Turtle()
    screen = turtle.Screen()

    screen.tracer(0, 0)

    t.penup()
    t.goto(-600, 500)
    t.pendown

    matrix = generate_map()
    draw_map(matrix, t)

    screen.mainloop()


if __name__ == "__main__":
    main()
