from flask import Flask, render_template, request
import json
import base64, requests, sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__)   # Flask constructor 
  
# A decorator used to tell the application 
# which URL is associated function 
@app.route('/')       
def index_page(): 
    return render_template("index.html")

@app.post('/recommend')
def recommend():
    auth_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(auth_manager=auth_manager)

    song = request.form["song"]
    # artist = input("Artist name: ")

    # results = sp.search(q= f"track: {song} artist: {artist}")
    results = sp.search(q= f"track: {song}")
    
    #List of dictionaries where each dict is a song
    list = results["tracks"]["items"]
    return render_template("songs.html", )

  
if __name__=='__main__': 
   app.run()