from datetime import datetime
from multiprocessing.connection import Connection
from time import sleep
import smtplib

import requests

MY_LAT = 19.432608
MY_LON = -99.133209
MY_EMAIL = "email"
MY_PASSWORD = "email_password"

def email_alert():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg="Subject: ISS IS IN TOWN!\n\nLook up, the International Space Station is near your city!")


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LON,
        "tzid": "America/Mexico_City",
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    today = datetime.now()
    return not sunrise <= today.hour <= sunset

def is_iss_overhead():
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url=url)
    response.raise_for_status()

    data = response.json()["iss_position"]

    longitude = float(data["longitude"])
    latitude = float(data["latitude"])

    return MY_LAT - 5 <= latitude <= MY_LAT + 5 and MY_LON - 5 <= longitude <= MY_LON + 5

while True:

    if is_iss_overhead() and is_night():
        email_alert()
    else:
        print("ISS is in another castle.")
    sleep(60)