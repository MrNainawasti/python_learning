from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 15
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        self.fd(MOVE_DISTANCE)

    def move_down(self):
        self.bk(MOVE_DISTANCE)

    def reset_pos(self):
        self.goto(STARTING_POSITION)