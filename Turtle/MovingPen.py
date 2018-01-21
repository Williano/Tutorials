# Script: MovingPen.py
# Description: This program uses python's turtle graphics module to draw shapes,lines,
#              circles and text.
# Programmer: William Kpabitey Kwabla.
# Date: 27.05.17



# Importing the turtle module.
import turtle

# It moves the pen to (0, 50) from (0, 0).
turtle.goto(0, 50)

# It moves the pen to (50, -50)
turtle.penup()
turtle.goto(50, -50)
turtle.pendown()

# It changes the color to red and draws a circle with radius 50.
turtle.color("red")
turtle.circle(50)


