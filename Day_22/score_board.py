

from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self._left_score = 0
        self._right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(x=-100, y=200)
        self.write(self._left_score, align="center", font=("Tahoma", 80, "normal"))
        self.goto(x=100, y=200)
        self.write(self._right_score, align="center", font=("Tahoma", 80, "normal"))

    def l_point(self):
        self.clear()
        self._left_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.clear()
        self._right_score += 1
        self.update_scoreboard()

    def get_score(self):
        return self._left_score, self._right_score

    def game_over(self, score):
        self.clear()
        game_over = Turtle()
        game_over.color("white")
        game_over.penup()
        game_over.hideturtle()
        if self._left_score == score:
            self.write(f"Left Player Wins",
                       align="center", font=("Tahoma", 60, "normal"))

        elif self._right_score == score:
            self.write(f"Right Player wins",
                       align="center", font=("Tahoma", 60, "normal")