from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests

spoti = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope='playlist-modify-private',
        redirect_uri='http://example.com',
        client_id='',
        client_secret='',
        show_dialog=True,
        cache_path='token.txt'
    )
    )

usr = spoti.current_user()['id']
date= input('which year would you like to travel(yyyy-mm-dd): ')
billboard = []
url = f'https://www.billboard.com/charts/hot-100/{date}'
response = requests.get(url=url)
soup = BeautifulSoup(response.text,'html.parser')
billboard = soup.findAll('span',class_="chart-element__information__song text--truncate color--primary")
billboard = [song.getText() for song in billboard]

year = date.split('-')[0]

song_uris = []
for song in billboard:
    result = spoti.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
playlist = spoti.user_playlist_create(user=usr, name=f"{date} Billboard 100", public=False)

spoti.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

