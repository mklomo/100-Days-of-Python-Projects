"""
    This class creates the ball object
"""

from turtle import Turtle

import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self._xmove = 10
        self._ymove = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self._xmove
        new_y = self.ycor() + self._ymove
        self.goto(x=new_x, y=new_y)

    def bounce_y(self):
        self._ymove *= -1

    def bounce_x(self):
        self._xmove *= -1
