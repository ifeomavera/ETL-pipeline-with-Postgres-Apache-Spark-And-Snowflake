import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd

#Setting up credentials for OAuth 
client_id = 'e1579079c582472d998f11f720ae99e2'
client_secret = 'd908ce6a59fb4f1784921c5aca87951d'
redirect_uri = 'http://127.0.0.1:8888/callback'

# Setting up the Spotify OAuth
scope = 'user-top-read' 
sp_oauth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope, cache_path='.cache')

# Creating a Spotipy client
sp = spotipy.Spotify(auth_manager=sp_oauth)

#Getting top artists that alredy exist
top_artists = sp.current_user_top_artists(limit=50, time_range='long_term')

#A list to stroe the data
artist_ls = []

#Populating the artist list
for artist in top_artists['items']:
        artist_info = {
            'Artistname': artist['name'],
            'Genre': artist['genres'] if artist['genres'] else ['Unknown Genre'],
            'FamousLevel': artist['popularity']
        }
        artist_ls.append(artist_info)


#Creating a data frmae from the list  
df = pd.DataFrame(artist_ls)

#Converting the dataframe to a JSON file
df.to_json('topArtists.json', index=False)