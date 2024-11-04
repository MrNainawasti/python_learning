from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = ScoreBoard()

# organizing the keys to move the paddle
screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    
    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()
    
    # detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330:
        ball.paddle_bounce()

    # detect collision with left paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.paddle_bounce()

    # detect right paddle misses
    if ball.xcor() > 390:
        ball.reset_pos()
        score.l_update()

    # detect left paddle miss
    if ball.xcor() < -390:
        ball.reset_pos()
        score.r_update()

    # left player win
    if score.l_score == 3:
        score.game_over("LEFT")
        game_is_on = False

    # right player win
    if score.r_score == 3:
        score.game_over("RIGHT")
        game_is_on = False


screen.exitonclick()