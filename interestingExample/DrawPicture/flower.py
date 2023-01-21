import colorsys as color
import turtle as tur

tur.setup(900, 1600)
tur.speed(0)  # set moving speed
tur.width(2)
tur.bgcolor("black")
j_loop, i_loop = 35, 15
for j in range(j_loop):
    for i in range(i_loop):
        tur.color(color.hsv_to_rgb(i / i_loop, j / j_loop, 1))
        tur.right(90)
        tur.circle(200 - j * 4, 90)
        tur.left(90)
        tur.circle(200 - j * 4, 90)
        tur.right(180)
        tur.circle(50, 24)
tur.hideturtle()
tur.done()
