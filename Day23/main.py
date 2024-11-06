import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.title("Turtle Crossing Game")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

car_manager = CarManager()

score_board = ScoreBoard()

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.generate_car()
    car_manager.car_move()

    if player.ycor() > 260:
        player.reset_pos()
        score_board.level_increase()
        car_manager.increase_speed()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            score_board.game_over()
            game_is_on = False






screen.exitonclick()