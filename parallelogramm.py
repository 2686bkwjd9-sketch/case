import turtle

def parall(x,y,a,b,color):
    turtle.up()
    turtle.setposition(x,y)
    turtle.down()
    turtle.color(color)
    turtle.begin_fill()

    turtle.forward(a)
    turtle.left(60)
    turtle.forward(b)
    turtle.left(120)
    turtle.forward(a)
    turtle.left(60)
    turtle.forward(b)
    turtle.left(120)

    turtle.end_fill()

parall(-50,50,120,60,'green')
turtle.done()
