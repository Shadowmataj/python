from datetime import datetime
import requests
from config import PIXELA_TOKEN

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "shadowmat123"
GRAPH_ID = "graph1"
GRAPH_NAME = "Study Graph"
HEADERS = {
    "X-USER-TOKEN": PIXELA_TOKEN
}
user_params = {
    "token": PIXELA_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
#Create_User
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.json())

# graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
# graph_config = {
#     "id": GRAPH_ID,
#     "name": GRAPH_NAME,
#     "unit": "h",
#     "type": "float",
#     "color": "sora",
# }
# response = requests.post(url=graph_endpoint, json=graph_config, headers=HEADERS)
# response.raise_for_status()
# print(response.text)

pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you study today?"),
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=HEADERS)
print(response.text)



# today = datetime(year=2024, month=11,day=14)
#
# pixel_update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"
#
# update_config = {
#     "quantity": "12"
# }
#
# response = requests.put(url=pixel_update_endpoint, json=update_config, headers=HEADERS)
# print(response.text)

# response = requests.delete(url=pixel_update_endpoint, headers=HEADERS)
# print(response.text)