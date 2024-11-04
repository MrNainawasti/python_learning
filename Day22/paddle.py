from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(1,5)
        self.lt(90)
        self.penup()
        self.goto(position)
        
        
    def move_up(self):
        self.fd(40)
        
    def move_down(self):
        self.bk(40)
        