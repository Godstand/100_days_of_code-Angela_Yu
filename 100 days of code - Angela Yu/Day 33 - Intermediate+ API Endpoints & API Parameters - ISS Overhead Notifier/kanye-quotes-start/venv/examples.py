import datetime as dt
import smtplib
import time

import requests

MY_LAT = 6.524379
MY_LONG = 3.379206
my_email = "godstand.aimiuwu@gmail.com"
my_password = "Osadebamen12345+"


def iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    # if the ISS is close to my position
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


# My position
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


def currently_dark():
    response = requests.get("https://api.sunrise-sunset.org/json?", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[1])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[1])
    time_now_hour = dt.datetime.now().hour
    # and it is currently dark,
    if time_now_hour >= sunset or time_now_hour <= sunrise:
        return True


# BONUS: run the code every 60 secs
while True:
    time.sleep(60)
    if iss_overhead() and currently_dark():
        # send me an email to tell me to look up
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=my_email,
                                msg="Subject: The International Space Station\n\n "
                                    "The ISS is above you in the sky")
