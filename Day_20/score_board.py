from turtle import Turtle

ALIGNMENT = "center"

FONT = ("Tahoma", 20, "normal")


class ScoreBoard(Turtle):


    def __init__(self, score=0):
        super().__init__()
        self._score = score
        with open("high_score_data.txt", mode="r") as data_file:
            content = int(data_file.read())
            self._high_score = int(content)
        self.hideturtle()
        self.penup()
        self.color("white")
        self.sety(y=280)
        self.write(f"Score = {self._score} High Score: {self._high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self._score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score = {self._score} High Score: {self._high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self._score > self._high_score:
            self._high_score = self._score
            with open("high_score_data.txt", mode="w") as data_file:
                data_file.write(str(self._high_score))
        self._score = 0
        self.update_score()



