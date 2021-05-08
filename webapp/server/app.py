from flask import Flask,session,render_template,redirect,request
from dotenv import load_dotenv
import os
import module as md
import time
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()
app=Flask(__name__,static_folder='../frontend',template_folder='../frontend/views')

app.config['SESSION_TYPE']=os.getenv('SESSION_TYPE')    
app.config.update(
    SECRET_KEY=''+os.getenv('SECRET_KEY')
)


@app.route('/')
def home():
    return render_template('index.html')
    # return app.config['SECRET_KEY']

@app.route('/verify')
def login():
    redirect_link=(md.login()).get_authorize_url()
    return redirect(redirect_link)
    

@app.route('/account')
def manage_token():
    soauth=md.login()
    session.clear()
    code = request.args.get('code')
    token_info = soauth.get_access_token(code)
    session["token_info"] = token_info
    return redirect("spotanalyst")

# sp=spotipy.Spotify(auth=session.get('token_info').get('access_token'))

@app.route('/spotanalyst')
def welcome():
    session['token_info'], authorized = get_token(session)
    session.modified = True
    if not authorized:
        return redirect('/verify')
    # data = request.form
    while(True):
        current_song=spotipy.Spotify(auth=session.get('token_info').get('access_token')).current_user_playing_track()
        current_playing=current_song['item']['name']
        current_id= current_song['item']['uri']
        current_id=current_id.split(":")
        current_song_cover=current_song["item"]["album"]["images"][0]["url"]
        return render_template('spotanalyst.html',
                                current_playing=current_playing,
                                current_id=current_id[2],
                                current_song_cover=current_song_cover)
    

# Checks to see if token is valid and gets a new token if not
def get_token(session):
    token_valid = False
    token_info = session.get("token_info", {})

    # Checking if the session already has a token stored
    if not (session.get('token_info', False)):
        token_valid = False
        return token_info, token_valid

    # Checking if token has expired
    now = int(time.time())
    is_token_expired = session.get('token_info').get('expires_at') - now < 60

    # Refreshing token if it has expired
    if (is_token_expired):
        sp_oauth = md.login()
        token_info = sp_oauth.refresh_access_token(session.get('token_info').get('refresh_token'))

    token_valid = True
    return token_info, token_valid

if __name__ == '__main__':
    app.run(host='localhost', port=os.getenv('PORT'),debug=True)