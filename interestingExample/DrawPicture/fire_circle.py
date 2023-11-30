from turtle import *

bgcolor("black")
speed(0)
hideturtle()
for num in range(200):
    color("red")
    circle(num)
    color("orange")
    circle(num * 0.8)
    right(3)
    forward(3)
done()
