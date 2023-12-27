import math
import random
import turtle

import numpy

COLOURS = ['green', (0.5, 1, 0), 'yellow', 'orange', 'red', (0.5, 0, 0)]
MAP_SIZE = 100
SQUARE_WIDTH = 10


def square(a, color, t):
    t.pencolor(color)
    t.color(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(a)
        t.left(90)
    t.end_fill()


def generate_map():
    matrix = [[0.0] * MAP_SIZE for _ in range(MAP_SIZE)]
    n = 200

    for _ in range(n):
        i = random.randint(0, MAP_SIZE - 1)
        j = random.randint(0, MAP_SIZE - 1)
        matrix[i][j] = 4

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

    max_value = numpy.amax(matrix)

    for i in range(MAP_SIZE):
        for j in range(MAP_SIZE):
            matrix[i][j] = matrix[i][j] / max_value

    return matrix


def draw_map(matrix, t):
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


def main():
    t = turtle.Turtle()
    screen = turtle.Screen()

    screen.tracer(0, 0)

    t.penup()
    t.goto(-600, 500)
    t.pendown

    matrix = generate_map()
    draw_map(matrix, t)

    screen.mainloop()


if __name__ == '__main__':
    main()
