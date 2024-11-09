from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import random
import time

SPEED = 0.12

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

# changing the direction of snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

score = ScoreBoard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(SPEED)
    snake.move()
    
    if snake.collision():
        snake.reset()
        score.reset()
        
    # detect collision with food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        score.update_score()
        snake.extend()
    
    # detect collision with wall
    if snake.segments[0].xcor() > 295 or snake.segments[0].xcor() < -295:
        snake.reset()
        score.reset()
    elif snake.segments[0].ycor() > 270 or snake.segments[0].ycor() < -295:   
        snake.reset()
        score.reset()

screen.exitonclick()