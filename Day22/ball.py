from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.lt(20)
        self.penup()
        self.move_speed = 0.1

    def move(self):
        self.fd(10)

    def wall_bounce(self):
        new_heading = 360 - self.heading()
        self.setheading(new_heading)

    def paddle_bounce(self):
        self.move_speed *= 0.9
        new_heading = 180 - self.heading()
        self.setheading(new_heading)

    def reset_pos(self):
        """resets the position of the ball at center and
        starts moving towards opposite direction"""
        self.move_speed = 0.1
        self.goto(0,0)
        new_heading = 180 - self.heading()
        self.setheading(new_heading)
