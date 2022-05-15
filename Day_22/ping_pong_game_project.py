"""
    Creating the ping-pong game
"""
# TODO : 1 : Create the Screen

from turtle import Screen

from paddle import Paddle

from ball import Ball

from score_board import  ScoreBoard

import time


LEFT_PADDLE_STARTING_POSITION = (-370, 0)

RIGHT_PADDLE_STARTING_POSITION = (370, 0)

WINNING_SCORE = 10

screen = Screen()

screen.bgcolor("black")

screen.setup(width=800, height=600)

screen.title("Marvin's Ping Pong Game")

screen.tracer(0)

# TODO : 2 : Create and Move the paddle
# TODO : 3 : Create another paddle

left_paddle = Paddle(start_position=LEFT_PADDLE_STARTING_POSITION)

right_paddle = Paddle(start_position=RIGHT_PADDLE_STARTING_POSITION)

# TODO : 4 : Create the ball and make it move and Score Board

ball = Ball()

score_board = ScoreBoard()


screen.listen()
screen.onkey(fun=left_paddle.move_up, key="e")
screen.onkey(fun=left_paddle.move_down, key="z")
screen.onkey(fun=right_paddle.move_up, key="u")
screen.onkey(fun=right_paddle.move_down, key="n")

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)
    # TODO : 5 : Detect Collision with the wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()

    # TODO : 6 : Detect Collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 335 or ball.distance(left_paddle) < 50 and ball.xcor() < -335:
        ball.bounce_x()
        ball.move_speed *= 0.8

    # TODO : 7 : Detect when paddle misses
    # TODO : 8 : Keep Score
    if ball.xcor() < -380:
        # Update Score for Right Player
        score_board.r_point()
        ball.home()
        ball.bounce_x()

    elif ball.xcor() > 380:
        # Update score for Left Player
        score_board.l_point()
        ball.home()
        ball.bounce_x()

    left_player_score, right_player_score = score_board.get_score()

    if (left_player_score == WINNING_SCORE) or (right_player_score == WINNING_SCORE):
        ball.home()
        game_is_on = False
        score_board.home()
        score_board.game_over(score=WINNING_SCORE)

screen.exitonclick()