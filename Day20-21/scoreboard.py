from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 16, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.update_score(0)


    def update_score(self, score):
        self.clear()
        self.penup()
        self.goto(-300,270)
        self.pendown()
        self.fd(600)
        self.goto(0, 270)
        self.write(f"Score: {score} ", align = ALIGNMENT , font = FONT)


    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align = ALIGNMENT , font = FONT)

