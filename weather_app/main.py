from venv import create

import requests
from twilio.rest import Client
from config import MY_NUMBER, TWILIO_PHONE_NUMBER, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN

API_KEY = "USE_YOUR_API_KEY"
URL = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": 19.432608,
    "lon": -99.133209,
    "cnt": 4,
    "appid": API_KEY
}

response = requests.get(URL, params=parameters)
response.raise_for_status()
weather_data = response.json()
weathers_list = weather_data["list"]
weather_codes_list = [weather["weather"][0]["id"] for weather in weathers_list if weather["weather"][0]["id"] < 700]

if len(weather_codes_list) > 0:
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages \
                    .create(
        body="Hallelujah It's raining day!",
        from_=TWILIO_PHONE_NUMBER,
        to=MY_NUMBER
    )
    print(message.status)