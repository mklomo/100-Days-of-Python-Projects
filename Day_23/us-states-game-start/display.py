from turtle import Turtle


class Display(Turtle):

    def __init__(self, state_name):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self._state_name = state_name

    def update_canvas(self, coord):
        self.goto(coord)
        self.write(self._state_name, align="center", font=("Tahoma", 14, "normal"))

    def game_over(self, score):
        self.home()
        self.write(f"Game Over! You Guessed {score} states right!", align="center", font=("Tahoma", 25, "normal"))

