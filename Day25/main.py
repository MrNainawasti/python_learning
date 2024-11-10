import turtle
import pandas

FONT = ("Arial", 24, "bold")

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# creating a dataFrame 
df = pandas.read_csv("50_states.csv")

# making a list of all the states extracting from the DataFrame
state_list = df.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    
    user_answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",prompt="What's another state's name?").title()
    if user_answer == "Exit":
        break
    
    if user_answer in state_list:
        guessed_states.append(user_answer)
        state_list.remove(user_answer)
        data = df[df.state == user_answer]
        x_cor = data.x.item()
        y_cor = data.y.item()
        writer.goto(x_cor, y_cor)
        writer.write(user_answer, align= "left")

    if len(guessed_states) == 50:
        writer.goto(0,0)
        writer.write("Congratulations!! You know all 50 states!!", align="center", font=FONT)
        screen.exitonclick()

missing_states = {
    "States": state_list
}

# storing all the missing states in a new DataFrame
new_data = pandas.DataFrame(missing_states)

# storing new DataFrame in a new csv file
new_data.to_csv("missing_states.csv")



