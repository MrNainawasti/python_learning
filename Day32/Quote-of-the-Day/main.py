import smtplib
import datetime as dt 
import random
import pandas

MY_EMAIL = "emailsender088@gmail.com"
MY_PASSWORD = "123Axyz40)MLde"  #password generated using app passwords from your email

def send_mail():
    with open("quotes.txt") as quotes:
        quotes_list = quotes.readlines()
        message = random.choice(quotes_list)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr= MY_EMAIL,
                            to_addrs= "receiver123@gmail.com",
                            msg= f"Subject:Quote of the Day\n\n{message}")




now = dt.datetime.now()
week_day = now.weekday()
if week_day == 0:
    send_mail()
