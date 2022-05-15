"""
    This script programs a turtle racing game using OOP
"""

from turtle import Turtle, Screen

import random

screen = Screen()

screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [120, 80, 40, 0, -40, -80]
all_turtles = []

for turtle_racer in range(6):
    turtle_name = Turtle(shape="turtle")
    turtle_name.color(colors[turtle_racer])
    turtle_name.penup()
    y_pos = y_position[turtle_racer]
    turtle_name.goto(x=-240, y=y_pos)
    all_turtles.append(turtle_name)


is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 215:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")

            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
            is_race_on = False
        rand_distance = random.randint(0, 7)
        turtle.forward(rand_distance)




screen.exitonclick()


