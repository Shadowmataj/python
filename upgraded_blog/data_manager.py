import requests

class DataManager:
    def __init__(self):
        self.posts = requests.get("https://api.npoint.io/617ff0fa36fab5c04d49").json()