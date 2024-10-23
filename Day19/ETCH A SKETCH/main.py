from turtle import Turtle, Screen

peter = Turtle()

def move_fd():
    peter.fd(10)

def move_bk():
    peter.bk(10)

def turn_left():
    peter.lt(10)

def turn_right():
    peter.rt(10)

def clear():
    # peter.clear()
    # peter.penup()
    # peter.home()
    # peter.pendown()
    peter.reset()



screen = Screen()
screen.listen()
screen.onkey(move_fd, "w")
screen.onkey(move_bk, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()