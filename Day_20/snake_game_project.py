"""
   This program builds the snake_object project in Python
"""

import time

from turtle import Screen

from snake import Snake

from food import Food

from score_board import ScoreBoard

# Create a screen and set it up

screen = Screen()

screen.setup(width=600, height=600)

# Change the background color of the screen and Title

screen.title("My Snake Game")

screen.bgcolor("black")

# Turn the screen tracer off
screen.tracer(0)

snake = Snake()

# TODO : 3 : Create snake_object food

food = Food()

# TODO : 5 : Create a Score Board

player_score = ScoreBoard()

# TODO : 2 : Move the Snake
screen.listen()
screen.onkey(fun=snake.move_up, key="Up")
screen.onkey(fun=snake.move_down, key="Down")
screen.onkey(fun=snake.move_left, key="Left")
screen.onkey(fun=snake.move_right, key="Right")

game_is_on = True


while game_is_on:
    # Update the screen
    screen.update()
    time.sleep(0.15)
    snake.motion()

    # TODO : 4: Detect Collision with Food
    # Detect collision with the snake

    if snake._head.distance(food) < 15:
        player_score.increase_score()
        snake.extend()
        food.refresh()

    # TODO : 6 : Detect Collision with the wall
    if snake._head.xcor() > 285 or snake._head.xcor() < -285 or snake._head.ycor() > 285 or snake._head.ycor() < -285:
        player_score.reset()
        snake.reset()

    # TODO : 7 : Detect Collision with Tail
    # Skip the head
    for segment in snake._snake_segments[1:]:
        #if head collides with any segment of the tail:
            #trigger game over

        if snake._head.distance(segment) < 5:
            player_score.reset()
            snake.reset()



# Defining Screen closing procedure

screen.exitonclick()
