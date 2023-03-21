import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

scope = "playlist-modify-public"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.search(q='genre:"edm"', type='track', limit=20)
tracks = results['tracks']['items']

playlist_name = 'My Python Playlist'
playlist_description = 'My playlist created using Python'

user_id = sp.me()['id']
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True, description=playlist_description)

track_ids = [track['id'] for track in tracks]
sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist['id'], tracks=track_ids)