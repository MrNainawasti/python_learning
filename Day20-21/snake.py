from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        
    def create_snake(self):
        for n in range(3):
            position = (n * -20, 0)
            self.add_segment(position)
    
    
    def add_segment(self, position):
        snake = Turtle("square")
        snake.color("white")
        snake.penup() 
        snake.goto(position)
        self.segments.append(snake)
    
    def extend(self):
        """add a new segment to the snake"""
        self.add_segment(self.segments[-1].position())
        
            
    def move(self):
        for n in range(len(self.segments)-1,0,-1):
            new_x = self.segments[n - 1].xcor()
            new_y = self.segments[n - 1].ycor()
            self.segments[n].goto(new_x, new_y)
        self.segments[0].fd(20)
        
    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
        
    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)
        
    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def collision(self):
        """detect collision with tail"""
        for segment in self.segments[1:]:
            if self.segments[0].distance(segment) < 10:
                return True