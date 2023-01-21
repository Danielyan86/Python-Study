import turtle
import math
import colorsys

screen = turtle.Screen()
screen.title('Pentaflake Fractal Colored - PythonTurtle.Academy')
screen.setup(1000, 1000)
screen.setworldcoordinates(-1000, -1000, 1000, 1000)
turtle.speed(0)
# turtle.hideturtle()
turtle.showturtle()
screen.tracer(0, 0)
turtle.fillcolor('dark cyan')


def pentagon(x, y, r, direction):  # x,y is the center
    turtle.up()
    turtle.goto(x, y)
    turtle.seth(direction)
    turtle.fd(r)
    turtle.left(126)
    turtle.down()
    c = colorsys.hsv_to_rgb((x + 1000) / 2000, 1, 0.7)
    turtle.color(c)
    turtle.begin_fill()
    for _ in range(5):
        turtle.fd(2 * r * math.sin(math.radians(36)))
        turtle.left(72)
    turtle.end_fill()


def pentaflake(x, y, r, direction, n):
    if n == 0:
        pentagon(x, y, r, direction)
        return

    r2 = r / (1 + 2 * math.cos(math.radians(36)))
    d = 2 * r2 * math.cos(math.radians(36))
    for _ in range(5):
        x2, y2 = x + d * math.cos(math.radians(direction)), y + d * math.sin(math.radians(direction))
        pentaflake(x2, y2, r2, direction, n - 1)
        direction += 72
    pentaflake(x, y, r2, direction + 180, n - 1)


pentaflake(0, 0, 1000, 90, 6)
screen.update()
