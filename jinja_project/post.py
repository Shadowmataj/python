import requests

class Post:
    def __init__(self):
        self.response_blogs = requests.get("https://api.npoint.io/3bfbaba2a7c8a5a7eaa3").json()