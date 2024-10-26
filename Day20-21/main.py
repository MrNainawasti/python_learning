from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import random
import time

SPEED = 0.1

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
current_score = 0

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(SPEED)
    snake.move()
    
    if snake.collision():
        game_is_on = False
        score.game_over()
        
    # detect collision with food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        current_score += 1
        score.update_score(current_score)
        snake.extend()
    
    # detect collision with wall
    if snake.segments[0].xcor() > 295 or snake.segments[0].xcor() < -295:
        game_is_on = False
        score.game_over()
    elif snake.segments[0].ycor() > 270 or snake.segments[0].ycor() < -295:   
        game_is_on = False
        score.game_over()

screen.exitonclick()