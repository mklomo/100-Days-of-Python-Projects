"""
    This project implements a program to draw the flumequine Hirst Spot Painting
"""

from color_extraction import BACKGROUND_COLOR, DOT_COLORS_LIST

from turtle import Turtle, Screen

import turtle

import random

# Setup the rgb color profile
turtle.colormode(255)

# Creating the turtle object
hirst_brush = Turtle()

# Hide the brush
hirst_brush.hideturtle()

# Change the appearance of the turtle
hirst_brush.shape("arrow")

# Check brush's starting coordinates
print(hirst_brush.pos())

# Set the x-coordinate and y-coordinate of hirst_brush
hirst_brush.penup()
starting_x_position = -200
starting_y_position = -200
hirst_brush.setpos(starting_x_position, starting_y_position)


# TODO : 1 : Create a painting with 10 by 10 rows or spots

# for circle_index in range(number_of_circles):
def draw_dots(paces, number_of_circles):
    """This function draws 10 circles"""
    for circle_index in range(number_of_circles):
        # Drop the hirst_brush on the canvas
        hirst_brush.pendown()
        # Draw a Circle and fill with random color
        dot_fill = random.choice(DOT_COLORS_LIST)
        hirst_brush.dot(20, dot_fill)
        # PenUp and move by 50
        hirst_brush.penup()
        hirst_brush.forward(paces)


# Define the Screen
screen = Screen()

# Define screen colormode
screen.colormode(255)

# Setting the screen color
screen.bgcolor(BACKGROUND_COLOR)

# TODO : 2 : Each DOT should be 20 in size and arrow moves at 50 paces
# Repositioning at the end of each line
for i in range(10):
    # Draw the dots for that line
    draw_dots(paces=50, number_of_circles=10)
    # penup and move to new starting position
    hirst_brush.penup()
    starting_y_position += 50
    hirst_brush.setpos(starting_x_position, starting_y_position)

# Checking the screen size
print(screen.screensize())

# When to exit screen
screen.exitonclick()
