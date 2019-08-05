"""
ALJ 08/04/2019
    - This function is responsible for fetching the playlists and songs per each
      playlist for a given Spotify user (username is passed to the function)

    - Client ID, Client Secret, and Redirect URI all need to be set per your 
      Spotify account here: https://developer.spotify.com/dashboard/login

    - Once the authorization is established via your web browser, the credentials 
      will be cached on your machine and no re-authorizing is needed

    - API python wrapper documentation:   https://spotipy.readthedocs.io/en/latest/#
"""

import spotipy
import spotipy.util as util

SPOTIPY_CLIENT_ID=''
SPOTIPY_CLIENT_SECRET=''
SPOTIFY_REDIRECT_URI=''

def fetch_spotify(username):
    def show_tracks(tracks):
        #define a blank list
        temp_dict = {}
        for i, item in enumerate(tracks['items']):
            track = item['track']
            #append the track per the given playlist to the list object
            temp_dict[track['artists'][0]['name']] = track['name']
        #return the list of tracks for the given playlist
        return temp_dict

    token = util.prompt_for_user_token(username, scope='user-library-read', client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIFY_REDIRECT_URI)
    
    if token:
        sp = spotipy.Spotify(auth=token)
        playlists = sp.user_playlists(username)
        user_playlist_info = {}
        for playlist in playlists['items']:
            if playlist['owner']['id'] == username:
                results = sp.user_playlist(username, playlist['id'],
                    fields="tracks,next")
                tracks = results['tracks']
                #we fetch the songs per playlist and throw into a dict object (in the function)
                tracks_dict = show_tracks(tracks)
                #update dictionary with playlist as key and dict object of tracks as the value
                user_playlist_info[playlist['name']] = tracks_dict
                while tracks['next']:
                    tracks = sp.next(tracks)
                    show_tracks(tracks)
    else:
        print("Can't get token for", username)

    #return a dict of dict with playlists and songs for given user
    return user_playlist_info
