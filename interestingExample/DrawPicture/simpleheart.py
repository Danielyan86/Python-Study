import turtle
import math

screen = turtle.Screen()
screen.title('Heart Animation - PythonTurtle.Academy')
screen.setup(1000, 1000)
screen.setworldcoordinates(-1000, -1000, 1000, 1000)
turtle.speed(10)
# turtle.hideturtle()

screen.tracer(0, 0)
turtle.color('red')


def draw_heart(alpha, d):
    r = d / math.tan(math.radians(180 - alpha / 2))
    turtle.up()
    turtle.goto(0, -d * math.cos(math.radians(45)))
    turtle.seth(90 - (alpha - 180))
    turtle.down()
    turtle.begin_fill()
    turtle.fd(d)
    turtle.circle(r, alpha)
    turtle.left(180)
    turtle.circle(r, alpha)
    turtle.fd(d)
    turtle.end_fill()


a = 220
sign = -1


def animate():
    global a, sign
    turtle.clear()
    draw_heart(a, 1000)
    screen.update()
    a += sign
    if a < 215:
        sign = -sign
    elif a > 220:
        sign = -sign
    screen.ontimer(animate, 50)


animate()
