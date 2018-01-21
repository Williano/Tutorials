# Script: TurtleGraphics.py
# Description: This program uses python's turtle graphics module to draw shapes,lines,
#              circles and text.
# Programmer: William Kpabitey Kwabla.
# Date: 27.05.17



# Importing the turtle module.
import turtle

# It shows the current location and direction of the turtle.
turtle.showturtle()

# It draws a text string.
turtle.write("Welcome to python")

# It moves the arrowhead 100 pixels forward to draw a line
# in the direction the arrow is pointing.
turtle.forward(100)

'''
It turns the arrowhead right 90 degrees, change the turtle’s color to red,
and move the arrowhead 50 pixels forward to draw a line.
'''
turtle.right(90)
turtle.color("red")
turtle.forward(100)


'''
It turns the arrowhead right 90 degrees, set the color to
green, and move the arrowhead 100 pixels forward to draw a line,
'''
turtle.right(90)
turtle.color("green")
turtle.forward(100)

'''
It turns the arrowhead right 45 degrees and move
it 80 pixels forward to draw a line
'''
turtle.right(45)
turtle.forward(80)
turtle.left(60)
turtle.forward(100)
