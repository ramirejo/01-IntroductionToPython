"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Jose Ramirez.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
green_turtle = rg.SimpleTurtle('turtle')
green_turtle.pen = rg.Pen('green', 5)
green_turtle.speed = 15
size = 100
for k in range(8):
    green_turtle.draw_circle(size)
    green_turtle.pen_up()
    green_turtle.left(200)
    green_turtle.forward(13)
    green_turtle.pen_down()
    size= size - 12

turtle2 = rg.SimpleTurtle('triangle')
turtle2.pen = rg.Pen("blue", 5)
turtle2.backward(100)
for k in range(15):
    turtle2.right(85)
    turtle2.forward(100)

window.close_on_mouse_click()