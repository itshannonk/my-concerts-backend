"""
All the Spotify stuff is handled in here.
"""
import requests

URL = "https://api.spotify.com/v1/playlists/"
ACC_TOKEN = 'BQBVLwLEeHYZgmUSdWJeurG_d7W0j6Edwd1ICM-Nxs_sLmLjdQXzkEoicB7bAk' \
            'r3H9xKWqX2j0kiKEZkMYbawq_GDGDTFoH0J0e2vw7LLBiBz2_dcd0JM5kEAGZA' \
            'xk89hGbfvRb1Nn75H9IPVepNAcif1i37PoDfXA'


def get_artist_names(playlist_id: str) -> list:
    """ Return a list of the artist names in the playlist with the id

    :param playlist_id: Spotify playlist id.
    :return: A list of artist names.
    """
    url = URL + playlist_id + '/tracks'
    params = {'playlist_id': playlist_id}
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
