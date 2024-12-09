import pandas
import datetime as dt 
import smtplib
from pathlib import Path
import random


MY_EMAIL = "senderemail088@gmail.com"
MY_PASSWORD = "123Axyz40)MLde"  #password generated using app passwords from your email
DIRECTORY_PATH = Path("letter_templates")
PLACEHOLDER = "[NAME]"


def select_random_letter(name):
    DIRECTORY_PATH.iterdir()
    files = [file for file in DIRECTORY_PATH.iterdir() if file.is_file()]
    random_template = random.choice(files)
    with open(random_template, mode="r") as random_letter:
        letter = random_letter.read()

    birthday_letter = letter.replace(PLACEHOLDER, name)
    return birthday_letter



def send_mail(letter, email):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr= MY_EMAIL,
                            to_addrs= email,
                            msg= f"Subject:Happy Birthday\n\n{letter}")



current_date = dt.datetime.now()
current_month = current_date.month
current_day = current_date.day


birthday_data = pandas.read_csv("birthdays.csv")
for (index, row) in birthday_data.iterrows():
    birth_month = row.month
    birth_day = row.day
    if birth_month == current_month and current_day == birth_day:
        name = row["name"]
        email = row.email
        birthday_card = select_random_letter(name)
        send_mail(birthday_card, email)








