import turtle
import math
import colorsys
import sys

screen = turtle
screen.title("5 Degree Square Spiral in a Square - PythonTurtle.Academy")
screen.setup(1000, 1000)
screen.setworldcoordinates(-1000, -1000, 1000, 1000)
screen.tracer(0, 0)
turtle.speed(8)
# turtle.hideturtle()
sys.setrecursionlimit(10000)


def draw_square(x, y, direction, length):
    turtle.up()
    turtle.goto(x, y)
    turtle.seth(direction)
    turtle.back(length / 2)
    turtle.left(90)
    turtle.back(length / 2)
    turtle.seth(direction)
    turtle.down()
    c = colorsys.hsv_to_rgb(0.9 * length / L, 1, 1)
    turtle.fillcolor(c)
    c = colorsys.hsv_to_rgb(0.9 * length / L, 1, 1)
    turtle.pencolor(c)
    turtle.begin_fill()
    for _ in range(4):
        turtle.fd(length)
        turtle.left(90)
    turtle.end_fill()


def square_spiral(x, y, direction, length):
    if length < 5:
        return

    draw_square(x, y, direction, length)
    square_spiral(
        x,
        y,
        direction + alpha,
        length / (math.sin(math.radians(alpha)) + math.cos(math.radians(alpha))),
    )


alpha = 0.1
L = 1600
square_spiral(0, 0, 0, L)
screen.done()
# screen.update()
