#Get Details from Spotify API using Spotipy. 
# Details we are trying to get: 1. Playlist of the user. 2. Songs in Playlist 3. Analysis of Songs in the playlist.#


import os
import spotipy
import webbrowser
import json,csv
import pandas as pd
from json.decoder import JSONDecodeError
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
#Importing Secure Keys using ENV (dotenv) Module
load_dotenv()


#User Credentials
client_id=os.getenv('SPOTIFY_CLIENT_ID')
client_secret=os.getenv('SPOTIFY_CLIENT_SECRET')
redirect_uri=os.getenv('REDIRECT_URI')
#Spotify Token Authentication
scope = os.getenv('SCOPES')

final_extract=".\\final_data\\extract_data\\"
final_stream='.\\final_data\\StreamingHistory\\'
spotify_data='.\\spotify_data\\vijayasai\\'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,client_secret=client_secret,
                                                redirect_uri=redirect_uri, scope=scope))

#Prints the Current User's Details
# user=sp.current_user()
# print(json.dumps(user,indent=2))

#Gets Current Song played by the user

# current_song=sp.current_user_playing_track()
# print(current_song)
# if(current_song==None):
#     print("No Song is Playing Right Now! Please check your Spotify Again!!")
# else:
#     with open(os.path.join(final_extract,'current_song.json'),'w') as current_song_output:
#         json.dump(current_song,current_song_output)
#     print("Name of Current Song: "+current_song['item']['name']+
#         "\nURI of the Song: "+current_song['item']['uri'])
#     uri_current_song = current_song['item']['uri']
#     audio_analysis= sp.audio_features(tracks=uri_current_song)
#     with open(os.path.join(final_extract,'current_song_analysis.json'),'w') as current_song_output:
#         json.dump(audio_analysis,current_song_output)
#     print("Audio Analysis for current song extracted successfully")





# Getting top tracks of the user
# top_tracks=sp.current_user_top_tracks(limit=20, offset=0, time_range='long_term')
# with open(os.path.join(final_extract,'top_tracks_long.json'),'w') as current_song_output:
#     json.dump(top_tracks, current_song_output)
# top_tracks_json=[]
# for i in range(len(top_tracks["items"])):
#     top_tracks_json.append(dict(trackName=top_tracks["items"][i]["name"],
#                                     trackURI=top_tracks["items"][i]["uri"]))
#     with open(os.path.join(final_extract,'top_tracks.json'),'w') as outfile:
#         json.dump(top_tracks_json, outfile)



results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name']," - ", track['id'])
# list_playlists=sp.current_user_playlists(limit=50, offset=0)
# print(json.dumps(list_playlists,indent=4))


# items_in_playlists=sp.playlist_items('2XIivRPHOyhKkm8FkphG9V', fields="items(track(name,id))", limit=100, offset=0, market=None, additional_types=('track', 'episode'))
# print(type(items_in_playlists))
# print(json.dumps(items_in_playlists,indent=4))
# print(items_in_playlists["items"][i]["track"]["id"])
# print(sp.audio_features(tracks=[items_in_playlists["items"][i]["track"]["id"]]),fields="danceability,energy,loudness,speechiness,acousticness")