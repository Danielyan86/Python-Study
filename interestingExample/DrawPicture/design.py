import turtle as t
import colorsys

t.bgcolor("black")
t.speed("fastest")
t.tracer(100)
t.pencolor("darkviolet")
hue = 0.7
t.hideturtle()


def func():
    global hue
    for i in range(4):
        global hue
        for i in range(4):
            color = colorsys.hsv_to_rgb(hue, 1, 1)
            hue += 0.001
            t.fillcolor(color)
            t.begin_fill()
            t.fd(100)
            t.right(18)
            t.fd(100)
            t.lt(22)
            t.end_fill()


for j in range(400):
    func()
    t.goto(8, 8)
    t.rt(188)

t.exitonclick()