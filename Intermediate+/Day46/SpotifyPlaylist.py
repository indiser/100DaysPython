from bs4 import BeautifulSoup
import requests
from datetime import datetime
import os
from dotenv import load_dotenv
import pprint

import spotipy
from spotipy.oauth2 import SpotifyOAuth


load_dotenv()

spotify_clint_id=os.environ.get("SPOTIFY_CLIENT_ID")
spotify_secret=os.environ.get("SPOTIFY_CLIENT_SECRET")
redirect_uri=os.environ.get("REDIRECT_URL")

# Scrape The website
# user_input=input("What year do you want to travel to? (YYYY-MM-DD):\n")

billboard_url="https://www.billboard.com/charts/hot-100/"

# response=requests.get(url=billboard_url+user_input)
bill_response=requests.get(url=billboard_url)


billboard_html=bill_response.text

soup=BeautifulSoup(billboard_html,"html.parser")
story_name=soup.select(selector="li > h3#title-of-a-story")

story_titles=[story.getText().strip() for story in story_name]


# Authentication
scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=spotify_clint_id,
    client_secret=spotify_secret,
    redirect_uri=redirect_uri,
    scope=scope,
    cache_path="token.txt",
    show_dialog=True,
    username="Rana",
    ))

user_id = sp.current_user()["id"]

# Crearte The playlist
create_playlist=sp.user_playlist_create(user=user_id,name="100-BillBoard-Hits",public=False,collaborative=False,description="100 hit songs from billboards")
playlist_id=create_playlist['id']

# Search for songs
song_uris=[]
for song in story_titles:
    result=sp.search(q=f"track:{song}",type="track",limit=1)
    # pprint.pprint(result)
    try:
        uri=result['tracks']['items'][0]['uri']
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Add songs to the playlist
sp.playlist_add_items(playlist_id=playlist_id,items=song_uris)

print(f"Spotify Playlist with {playlist_id} id has been created with {len(song_uris)} songs")