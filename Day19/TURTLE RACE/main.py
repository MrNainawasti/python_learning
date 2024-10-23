import turtle as t
import race
import random

race_on = False

screen = t.Screen()
screen.setup(width = 500, height = 400)

race.race_setup()
race.ready_turtles()

user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")

if user_bet:
    race_on = True

while race_on:
    for turtle in race.race_turtles:
        if turtle.xcor() > 200:
            winner = turtle.pencolor()
            if user_bet == winner:
                print(f"You won!! The {winner} turtle is the winner!" )
            else:
                print(f"You lose!! The {winner} turtle is the winner!" )
            race_on = False
        else:
            move = random.randint(0,10)
            turtle.fd(move)


screen.exitonclick()