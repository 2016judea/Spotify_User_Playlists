"""
ALJ 08/04/2019
    - This program allows a user to search for a Spotify username and list the 
      playlists and songs per each playlist for that given Spotify username

    - This program utilizes the open source library spotipy which can be installed
      using 'pip install spotipy' 
            GitHub repo located here: https://github.com/plamere/spotipy
"""
from fetch_spotify import fetch_spotify

def main():
    username = input("Enter the username of the Spotify user you would like to look up: ")
    user_playlist_info = fetch_spotify(username)
    print("\n")
    print("Looking up playlists for user: " + username)
    print("\n")
    print("Available playlists for viewing:")
    
    #iterate the dictionary listing out the playlists
    for key, value in user_playlist_info.items():
        print("  " + key)
    response = input("Enter the playlist you would like have tracks listed for: ")
    print("\n")
    
    for key, value in user_playlist_info.items():
        if response == key:
            found_playlist = True
            x = 0
            #we iterate the dictionary that matches the key value (playlist) entered by the user
            for key, value in user_playlist_info[key].items():
                x += 1
                print("   %d %32.32s %s" % (x, key, value))
    
    if found_playlist == False:
        print("Invalid playlist entered...")

if __name__ == '__main__':
    main()