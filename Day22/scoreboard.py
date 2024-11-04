from turtle import Turtle

FONT = ("courier", 20, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 250)
        self.write(self.l_score, align="center", font= FONT)
        self.goto(100, 250)
        self.write(self.r_score, align="center", font= FONT)

    def l_update(self):
        self.clear()
        self.l_score += 1
        self.goto(-100, 250)
        self.write(self.l_score, align="center", font= FONT)
        self.goto(100, 250)
        self.write(self.r_score, align="center", font= FONT)

    def r_update(self):
        self.clear()
        self.r_score += 1
        self.goto(100, 250)
        self.write(self.r_score, align="center", font= FONT)
        self.goto(-100, 250)
        self.write(self.l_score, align="center", font= FONT)

    def game_over(self, player):   
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font= FONT)
        self.goto(0, -25)
        self.write(f"{player} PLAYER WIN!", align="center", font= FONT)