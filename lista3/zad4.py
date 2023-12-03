import math
from turtle import Screen, backward, forward, rt, speed

screen = Screen()


def kolko(N, b):
    for i in range(N):
        tmp_b = b + 20 * math.sin(i * 180 / N)
        forward(tmp_b)
        backward(tmp_b)
        rt(360 / N)


speed('fastest')

N = 400
b = 200
kolko(N, b)


screen.mainloop()
