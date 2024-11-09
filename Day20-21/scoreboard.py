from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 16, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.color("white")
        self.update_score()


    def update_score(self):
        self.clear()
        self.penup()
        self.goto(-300,270)
        self.pendown()
        self.fd(600)
        self.goto(0, 270)
        self.score += 1
        self.write(f"Score: {self.score - 1}  High Score: {self.high_score}", align = ALIGNMENT , font = FONT)


    def reset(self):
        """update high score"""
        if self.score > self.high_score:
            self.high_score = self.score - 1
        
        with open("data.txt", mode="w") as data:
            data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

