import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 27.717245
MY_LONG = 85.323959

MY_EMAIL = "mailsender088@gmail.com"
MY_PASSWORD = "abxM120)#AxB"

def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if  MY_LAT - 5  <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5  <= iss_longitude <= MY_LONG + 5:
        return True


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 6    #UTC + 6hrs
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 6      #UTC + 6hrs

    time_now = datetime.now().hour

    if time_now >= sunset and time_now <= sunrise:
        return True
   

def send_mail():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr= MY_EMAIL,
                            to_addrs= "receiver088@gmail.com",
                            msg= f"Subject:Look Up\n\nSup Bruv!! Look up!! The ISS is above you in the sky!")

while True:
    #running the code every 60 sec
    time.sleep(60)
    
    if iss_overhead() and is_dark():
        send_mail()






