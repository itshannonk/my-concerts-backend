"""
All the Spotify stuff is handled in here.
"""
import requests

URL = "https://api.spotify.com/v1/playlists/"
ACC_TOKEN = 'be1f18ddbbb84db996b23f1222c33d17 f0b5f383f0294a30835adfae60119dca'


def get_artist_names(playlist_id: str) -> list:
    """ Return a list of the artist names in the playlist with the id

    :param playlist_id: Spotify playlist id.
    :return: A list of artist names.
    """
    url = URL + playlist_id + '/tracks'
    params = {'playlist_id': playlist_id,
              'client_id': 'be1f18ddbbb84db996b23f1222c33d17',
              'client_secret': 'f0b5f383f0294a30835adfae60119dca'}
    response = requests.get(url=url, params=params,
                            headers={'Authorization':
                                     'Bearer ' + ACC_TOKEN}).json()

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
