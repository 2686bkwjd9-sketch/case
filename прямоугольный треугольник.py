import turtle
import math
def right_triangle(x, y, a, color):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color(color)
    turtle.begin_fill()
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(135)
    turtle.forward(a * math.sqrt(2))
    turtle.end_fill()
right_triangle(-50, 50, 100, "blue")
turtle.done()