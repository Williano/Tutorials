# Script: OlympicSymbol.py
# Description: This program uses python's turtle graphics module to 
#              drawing the Olympics rings logo.
# Programmer: William Kpabitey Kwabla.
# Date: 27.05.17



# Importing the turtle module.
import turtle

'''
Drawing a blue circle by moving the pen using the penup() and pendown() functions
and goto() function without drawing anything and drawing a circle using the
circle() function.
'''
turtle.color("blue")
turtle.penup()
turtle.goto(-110, -25)
turtle.pendown()
turtle.circle(45)

# Drawing a black circle.
turtle.color("black")
turtle.penup()
turtle.goto(0, -25)
turtle.pendown()
turtle.circle(45)

# Drawing a red circle.
turtle.color("red")
turtle.penup()
turtle.goto(110, -25)
turtle.pendown()
turtle.circle(45)

# Drawing a yellow circle.
turtle.color("yellow")
turtle.penup()
turtle.goto(-55, -75)
turtle.pendown()
turtle.circle(45)

# Drawing a green circle.
turtle.color("green")
turtle.penup()
turtle.goto(55, -75)
turtle.pendown()
turtle.circle(45)

'''
Pausing the program to allow the user to close
the Python Turtle Graphics windows to
avoid it from closing immediately it finishes.
'''
turtle.done() 
