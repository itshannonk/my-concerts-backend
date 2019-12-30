"""
This is the file in which we will test the Spotify API.
"""
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# client_credentials_manager = SpotifyClientCredentials("be1f18ddbbb84db996b23f1222c33d17", "f0b5f383f0294a30835adfae60119dca")
# spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

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

# results = spotify.search(q='playlist:' + 'indie or something', type='playlist')
# print(results)

"""
The following functions may be helpful:
    1. current_user_playlists(limit=50, offset=0)
    2. user_playlist(user, playlist_id=None, fields=None)
    3. user_playlists(user, limit=50, offset=0)
"""
import requests

"""# Get playlist URL
playlist = input("Insert playlist URL: ")
playlist_id = playlist[34:playlist.find('?si=')]

accessToken = 'BQCL3z6IDTYP353oNWAkqNHosp8kK5cUBLFdlRkrlUfs4lSuUQlbskLDADtol' \
              'nf97ZSD_nQILrzLbsABeM3a3Py0In2WUadMcgoWP-GI0IgBRhHUY86MOklQZP' \
              'asdC-d2juj64WOBRiU6hUeN9cRrFH7Q-L9cheiYw'

URL = "https://api.spotify.com/v1/playlists/" + playlist_id + "/tracks"
PARAMS = {'playlist_id': playlist_id}
r = requests.get(url=URL, params=PARAMS,  headers={
               'Authorization': 'Bearer ' + accessToken
            })
data = r.json()
if 'error' in data:
    print(data['error']['message'])
else:
    for item in data['items']:
        # print(item['track']['name'])
        artists = []
        for artist in item['track']['artists']:
            artists.append(artist['name'])
        # print(item['track'])
        print(item['track']['name'] + " by " + ", ".join(artists))"""

# POST REQUEST -----------------------------------------------------------------
"""client = 'be1f18ddbbb84db996b23f1222c33d17:f0b5f383f0294a30835adfae60119dca'
API_ENDPOINT = 'https://accounts.spotify.com/api/token'

data = {'grant_type': 'client_credentials'}
headers = {'Authorization': 'Basic ' + client}
r = requests.post(url=API_ENDPOINT, data=data,  headers=headers)

# response = requests.post(url=API_ENDPOINT, data=data)
print(r.text)"""


# THIS ONE WORKS!! -------------------------------------------------------------
"""client_id = 'be1f18ddbbb84db996b23f1222c33d17'
client_secret = 'f0b5f383f0294a30835adfae60119dca'
grant_type = 'client_credentials'

body_params = {'grant_type': grant_type}
url = 'https://accounts.spotify.com/api/token'
response = requests.post(url, data=body_params, auth=(client_id, client_secret))
print(response.json())"""

# AUTHENTICATION REQUEST -------------------------------------------------------
"""URL = 'https://accounts.spotify.com/authorize'
PARAMS = {'client_id': 'be1f18ddbbb84db996b23f1222c33d17',
          'response_type': 'code',
          'redirect_uri': 'https://github.com/itshannonk/csc207-project-backend'
          }
r = requests.get(URL, PARAMS)
print(r.text)"""

URL = 'https://us-central1-playlist-to-concert.cloudfunctions.net/get_all_concerts'
PARAMS = {'playlist_id': '7MbjdEGQQ5hEtTyWEzjX63',
          'city': 'Toronto'
          }
r = requests.get(URL, PARAMS)
print(r.text)


if __name__ == "__main__":
    print("done")
    # playlist = input("Insert playlist URL: ")
    # playlist_id = playlist[34:playlist.find('?si=')]
    # print("hey!")
