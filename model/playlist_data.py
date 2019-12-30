"""
All the Spotify stuff is handled in here.
"""
import requests

URL = "https://api.spotify.com/v1/playlists/"
CLIENT_ID = 'be1f18ddbbb84db996b23f1222c33d17'
CLIENT_SECRET = 'f0b5f383f0294a30835adfae60119dca'


def get_new_access_token() -> str:
    """ Return new credit credential access token.

    :return: Access token.
    """
    body_params = {'grant_type': 'client_credentials'}
    url = 'https://accounts.spotify.com/api/token'
    response = requests.post(url, data=body_params,
                             auth=(CLIENT_ID, CLIENT_SECRET))
    return response.json()['access_token']


def get_artist_names(playlist_id: str) -> list:
    """ Return a list of the artist names in the playlist with the id

    :param playlist_id: Spotify playlist id.
    :return: A list of artist names.
    """
    url = URL + playlist_id + '/tracks'
    params = {'playlist_id': playlist_id,
              'client_id': CLIENT_ID,
              'client_secret': CLIENT_SECRET}
    headers = {'Authorization': 'Bearer ' + get_new_access_token()}
    response = requests.get(url=url, params=params, headers=headers).json()

    if 'error' in response:
        return response['error']['message']
    else:
        artists = []
        for item in response['items']:
            for artist in item['track']['artists']:
                artists.append(artist['name'])
            # print(item['track'])
            # print(item['track']['name'] + " by " + ", ".join(artists))
        return list(set(artists))


if __name__ == '__main__':
    print(get_artist_names('4LNYEMOoROyKkNtSGbHqef'))
    # print(get_new_access_token())
