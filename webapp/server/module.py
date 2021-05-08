import os
import spotipy
from spotipy import SpotifyOAuth
from dotenv import load_dotenv
#Importing Secure Keys using ENV (dotenv) Module
load_dotenv()

#User Credentials
client_id=os.getenv('SPOTIFY_CLIENT_ID')
client_secret=os.getenv('SPOTIFY_CLIENT_SECRET')
redirect_uri=os.getenv('REDIRECT_URI')
#Spotify Token Authentication
scope = os.getenv('SCOPES')

def login():
    soauth = spotipy.oauth2.SpotifyOAuth(client_id = client_id, client_secret = client_secret,
                                            redirect_uri = redirect_uri, scope = scope)
    return soauth