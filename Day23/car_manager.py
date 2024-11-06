from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():

    def __init__(self):
        self.all_cars = []
        road = Turtle()
        road.hideturtle()
        road.penup()
        road.goto(-300,250)
        road.pendown()
        road.fd(600)
        road.penup()
        road.goto(-300,-250)
        road.pendown()
        road.fd(600)        
        self.speed = STARTING_MOVE_DISTANCE


    def generate_car(self):
        num = random.randint(1,4)
        if num == 1:
            car = Turtle("square")
            car.shapesize(1,2)
            car.penup()
            car.color(random.choice(COLORS))
            y_cor = random.randint(-240,240)
            car.goto(300, y_cor)
            self.all_cars.append(car)


    def car_move(self):
        for car in self.all_cars:
            car.bk(self.speed)


    def increase_speed(self):
        self.speed += MOVE_INCREMENT
        for car in self.all_cars:
            car.bk(self.speed)