import turtle as t 

def race_setup():
    """sets up the race pitch"""
    y = 175
    volunteer = t.Turtle()
    volunteer.speed(10)
    volunteer.pensize(5)
    volunteer.penup()
    volunteer.goto(-210, y)
    volunteer.rt(90)
    volunteer.pendown()
    volunteer.fd(300)
    volunteer.penup()
    volunteer.goto(220, y)
    volunteer.pendown()
    volunteer.fd(300)
    for n in range(7):
        volunteer.penup()
        volunteer.goto(-210, y)
        volunteer.setheading(0)
        volunteer.pendown()
        volunteer.fd(430)
        y -= 50
        
    volunteer.hideturtle() 


def ready_turtles(): 
    """sets up all the turtles in starting position""" 
    y = 150
    for turtle_index in range(6):
        peter = t.Turtle(shape = "turtle")  
        peter.color(colors[turtle_index])
        race_turtles.append(peter)
        peter.penup()
        peter.goto( -230, y )
        y -= 50
        
race_turtles = []
colors = ["red", "green", "black", "blue", "orange", "purple"]