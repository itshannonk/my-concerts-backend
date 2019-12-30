"""
This is the file in which we will test the Spotify API.
"""
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials("be1f18ddbbb84db996b23f1222c33d17", "f0b5f383f0294a30835adfae60119dca")
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

"""playlists = spotify.user_playlists('spotify')
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = spotify.next(playlists)
    else:
        playlists = None
"""
# spotify = spotipy.Spotify() # initialize instance of spotify
# results = spotify.search(q='artist:' + "Summer Salt", type='artist')
# print(results['artists']['items'][0]['name'])

results = spotify.search(q='playlist:' + 'indie or something', type='playlist')
# print(results)

"""
The following functions may be helpful:
    1. current_user_playlists(limit=50, offset=0)
    2. user_playlist(user, playlist_id=None, fields=None)
    3. user_playlists(user, limit=50, offset=0)
"""
import requests
accessToken = 'BQAC4ZHP2F7U79-rpaUPY5_s-v2VXVTamnnOo9WGZJTva-8Jk7OjbU0DnX' \
              'YA6cY0pJv0e0phHyjxCraBpnI3kK3XVVkUEj4HnT5yfFYfRutTE2z4LkGD' \
              'emj39OXtHU3fRWTmwpsJyF3zzdOMvkonNzo6oJ-faeDvxQ'

URL = "https://api.spotify.com/v1/playlists/7uiNxgG7eIUaRbYRDrPoIV/tracks"
playlist_id = '7uiNxgG7eIUaRbYRDrPoIV'
PARAMS = {'playlist_id': playlist_id, 'tracks': 'tracks'}
r = requests.get(url=URL, params=PARAMS,  headers={
               'Authorization': 'Bearer ' + accessToken
            })
data = r.json()
for item in data['items']:
    # print(item['track']['name'])
    print(item['track'])

if __name__ == "__main__":
    print("hey!")
