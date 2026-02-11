import turtle

def ravn_triangle(x,y,a,color):
    turtle.up()
    turtle.setposition(x,y)
    turtle.down()
    turtle.color(color)
    turtle.begin_fill()

    turtle.forward(a)
    turtle.left(120)
    turtle.forward(a)
    turtle.left(120)
    turtle.forward(a)

    turtle.end_fill()

ravn_triangle(-50,50,100,"blue")
