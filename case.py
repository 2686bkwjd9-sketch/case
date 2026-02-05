# Case-study #1
# Developers: Voronina A., Sankina A., Grishina D.

import turtle 

def square(x,y,a,color): 
  turtle.up()
  turtle.setposition(x, y)
  turtle.down()
  turtle.color(color)
  turtle.begin_fill()

  turtle.forward(a)
  turtle.right(90)
  turtle.forward(a)
  turtle.right(90)
  turtle.forward(a)
  turtle.right(90)
  turtle.forward(a)
  turtle.right(90)

  turtle.end_fill()

square(-50, 50, 100, "red")
turtle.done()
