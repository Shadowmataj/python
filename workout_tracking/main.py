from datetime import datetime
import os

import requests

URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutritionix_headers = {
    "x-app-id": os.environ.get("NUTRITIONIX_APP_ID"),
    "x-app-key": os.environ.get("NUTRITIONIX_KEY"),
}

parameters = {
    "query": input("Tell me which exercises you did: "),
    "age": 31,
    "weight_kg": 100,
    "height_cm":  179
}

response = requests.post(URL, json=parameters, headers=nutritionix_headers)

data = response.json()



sheety_url = os.environ.get("SHEETY_URL")
today = datetime.now()

data_bodies = [
    {
    "workout": {
        "date": today.strftime("%d/%m/%Y"),
        "time": today.strftime("%H:%M:%S"),
        "exercise": exercise["name"],
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"]
        }
    }
    for exercise in data["exercises"]]

sheety_headers = {
    "Authorization": os.environ.get("SHEETY_TOKEN"),
}

for body in  data_bodies:
    sheety_response = requests.post(sheety_url, json=body, headers=sheety_headers)
    print(sheety_response.text)