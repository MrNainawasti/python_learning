BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import random
import pandas

current_card = {}

# DataFrame
try:
    df = pandas.read_csv("data/remain_to_learn.csv")
    to_learn = df.to_dict(orient="records")

except FileNotFoundError:
    df = pandas.read_csv("data/french_words.csv")
    to_learn = df.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title, text = "French", fill= "black")
    canvas.itemconfig(word, text = current_card["French"], fill= "black")
    canvas.itemconfig(flash_card, image=card_front_img)
    flip_timer = window.after(4000, flip_card)

def known_card():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/remain_to_learn.csv", index=False)
    next_card()

def flip_card():
    canvas.itemconfig(flash_card, image=card_back_img)
    canvas.itemconfig(title, text = "English", fill= "white")
    canvas.itemconfig(word, text = current_card["English"], fill= "white")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("FlashCard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.after(4000, flip_card)
flip_timer = window.after(4000, flip_card)

# images
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

# flash card canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card = canvas.create_image(410, 270, image=card_front_img)
title = canvas.create_text(400, 150, font=("arial", 40, "italic"))
word = canvas.create_text(400, 300, font=("arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan= 2)

# buttons
wrong_button = Button(image=wrong_img, command=next_card, bg=BACKGROUND_COLOR ,highlightthickness=0)
wrong_button.grid(row=1, column= 0)

right_button = Button(image=right_img, command=known_card, bg=BACKGROUND_COLOR ,highlightthickness=0)
right_button.grid(row=1, column= 1)

next_card()



window.mainloop()