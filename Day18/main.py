import turtle as t 
import random


color_list = [(1, 9, 30),(121, 95, 41), (72, 32, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100),
              (93, 1, 21), (178, 140, 170), (151, 92, 115), (35, 90, 26), (6, 154, 73),
              (205, 63, 91), (168, 129, 78), (3, 78, 28), (1, 64, 147), (221, 179, 218)]

t.colormode(255)
peter = t.Turtle()
peter.hideturtle()
peter.speed(0)
peter.penup()
peter.goto(-200,-200)
peter.pendown()



def draw():
    for x in range(10):
        peter.dot(20, random.choice(color_list))
        peter.penup()
        peter.fd(50)
        peter.pendown()

for y in range(1, 11):
    draw()
    peter.penup()
    peter.goto(-200, -200 + 50 * y)
    peter.pendown()

screen = t.Screen()
screen.exitonclick()