from turtle import Turtle
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-200, 250)
        self.write(f"level:{self.level}", align="center", font= FONT)

    def level_increase(self):
        self.clear()
        self.level += 1
        self.write(f"level:{self.level}", align="center", font= FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font= FONT)        