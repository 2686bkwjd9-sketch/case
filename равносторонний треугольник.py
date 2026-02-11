import turtle
import math
def rtriangle(x, y, a, color):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(a)
        turtle.left(120)
    turtle.end_fill()
rtriangle(-50, 0, 80, "hotpink")
turtle.done()
