"""
    This script implements the paddle for the Ping Pong Project
"""

from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, start_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(start_position)

    def move_up(self):
        if self.ycor() < 245:
            new_y = self.ycor() + 20
            self.sety(new_y)

    def move_down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - 20
            self.sety(new_y)



