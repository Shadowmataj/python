from venv import create

import requests
from twilio.rest import Client

API_KEY = "USE_YOUR_API_KEY"
URL = "https://api.openweathermap.org/data/2.5/forecast"
PHONE_NUMBER = "USE_YOUR_TWILIO_PHONE_NUMBER"
account_sid = "USE_YOUR_TWILIO_ACCOUNT_SID"
auth_token = "USE_YOUR_TWILIO_TOKEN"

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
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
        body="Hallelujah It's raining day!",
        from_=PHONE_NUMBER,
        to="+525568897613"
    )
    print(message.status)