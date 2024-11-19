from bs4 import BeautifulSoup
from datetime import date
import requests
import spotipy
import os
import ast

scope = "playlist-modify-private"
is_playlist_created = False

with open(".cache-ffsw852wpjxd4b6ab693vw4j3") as file:
    token_info = file.read()
    token_dict = ast.literal_eval(token_info)
    token = token_dict["access_token"]

spotify_auth = spotipy.oauth2.SpotifyOAuth(
    client_id=os.environ.get("SPOTIFY_CLIENT_ID"),
    client_secret=os.environ.get("SPOTIFY_CLIENT_SECRET"),
    redirect_uri="http://example.com", scope=scope, username=os.environ.get("SPOTIFY_USER_NAME"),
    requests_timeout=10)

spotify_api = spotipy.client.Spotify(auth=token, requests_session=True, oauth_manager=spotify_auth,
                        requests_timeout=5, status_forcelist=None, retries=3,
                        status_retries=3, backoff_factor=0.3)

def token_expired():
    return spotify_auth.is_token_expired(token_info=token_dict)

def get_token():
    spotify_auth.refresh_access_token()

def get_id_songs() -> list:
    songs_id_list = []
    acc=0
    for song in songs_info:
        spotify_search_response = spotify_api.search(
            q=f"remaster artist: {song["artist"]} track:{song["song"]} year:{formated_date.year}".replace(" ", "%2025"),
            limit=10,
            type="track")
        for item in spotify_search_response["tracks"]["items"]:
            if item["artists"][0]["name"].title() == song["artist"].title() and song["song"].title() in item["name"].title():
                songs_id_list.append(item["id"])
                acc += 1
                break

    print(f"{acc} songs were found")
    return songs_id_list


def create_playlist():
    global is_playlist_created
    client = spotipy.client.Spotify(auth=token)
    client_id = client.current_user()["id"]


    spotify_url = f"https://api.spotify.com/v1/users/{client_id}/playlists"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    playlist_name = f"{date_to_search} Billboard hot-100"

    with open("registered_playlists.txt") as playlists_file:
        lines = playlists_file.readlines()
        registered = [line.strip() for line in lines]
        if playlist_name in registered:
            print("The playlist has already been created.")
        else:
            body = {
                "name": playlist_name,
                "description": f"A playlist that includes come of the top-100 songs from {months_dict[formated_date.month]} {formated_date.day}, {formated_date.year} ",
                "public": True
            }

            spotify_response = requests.post(url=spotify_url, json=body, headers=headers)
            playlist_id = spotify_response.json()["id"]

            spotify_api.user_playlist_add_tracks(user=client_id, playlist_id=playlist_id, tracks=get_id_songs())

            with open("registered_playlists.txt", "a") as record_file:
                record_file.write(f"{playlist_name}\n")


    is_playlist_created = not is_playlist_created



months_dict = {
    1: "january",
    2: "february",
    3: "march",
    4: "april",
    5: "may",
    6: "june",
    7: "july",
    8: "august",
    9: "september",
    10: "october",
    11: "november",
    12: "december",
}


#---------------------------Billboard top 100-----------------------------#
date_to_search = input("Which year do you want to travel? Type the date in this format YYYY-MM-DD: ")
formated_date = date.fromisoformat(date_to_search)
url =  "https://www.billboard.com/charts/hot-100"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(url=f"{url}/{date_to_search}", headers=header)
soup = BeautifulSoup(response.text, "html.parser")

songs_titles = soup.select("li ul li h3", attrs={"id": "title-of-a-story"})
songs_artists = soup.find_all(name="span", class_= "a-no-trucate")

songs_info = [{"artist": songs_artists[number].text.strip(), "song": songs_titles[number].text.strip()} for number in range(len(songs_artists))]



#---------------------------Spotify--------------------------------------#

while not is_playlist_created:
    if not token_expired():
        create_playlist()
    else:
        get_token()
