"""
This will be the file containing my cloud functions.
"""
from flask import Request
from model import playlist_data, concert_data
import json


def get_all_concerts(request: Request):
    """ Return a dict of all concerts in the playlist with the given id.

    :param request: flask.Request object.
    :return: A json object containing the concerts of all artists in the playlist.
    """
    playlist_id = request.args['playlist_id']
    city = request.args['city']

    # Should it return a list of json objects?
    artists = playlist_data.get_artist_names(playlist_id)
    concerts = []

    for artist in artists:
        concerts.append(concert_data.get_event_key_city(artist, city))

    return {'concerts': artists_with_shows(concerts)}


def get_concert(request: Request):
    """ Return a concert's data based on that concert's id.

    :param request: flask.Request object.
    :return: A json object containing the concert data.
    """
    concert_id = request.args['concert_id']
    pass


def get_concerts_filtered(request: Request):
    """ Return a dict of all concerts based on the given filters.

    :param request: flask.Request object.
    :return: A json object containing the concert data.
    """
    playlist_id = request.args['playlist_id']

    artists = playlist_data.get_artist_names(playlist_id)
    concerts = []
    search_dict = request.args.to_dict()

    for artist in artists:
        search_dict['keyword'] = artist
        concerts.append(concert_data.get_event_key_city(search_dict))

    return {'concerts': artists_with_shows(concerts)}


def artists_with_shows(concerts: list) -> list:
    """ Return a list containing artists with upcoming concerts

    :param concerts: A list containing info for all artists.
    :return: List containing concert info.
    """
    shows = []
    for concert in concerts:
        if '_embedded' in concert:
            shows.append(concert)
    return shows


# TODO: Create a separate testing file for this
def get_all_concerts_test(request: dict):
    """ Return a list of all concerts in the playlist with the given id.

    :param request: flask.Request object.
    :return: A json object containing the concerts of all artists in the playlist.
    """
    playlist_id = request['playlist_id']
    city = request['city']

    # Should it return a list of json objects?
    artists = playlist_data.get_artist_names(playlist_id)
    concerts = []

    for artist in artists:
        concerts.append(concert_data.get_event_key_city(artist, city))

    return {'concerts': artists_with_shows(concerts)}


def get_concerts_filtered_test(request: dict):
    """ Return a dict of all concerts based on the given filters.

    :param request: flask.Request object.
    :return: A json object containing the concert data.
    """
    playlist_id = request['playlist_id']

    artists = playlist_data.get_artist_names(playlist_id)
    concerts = []
    search_dict = request

    for artist in artists:
        search_dict['keyword'] = artist
        concerts.append(concert_data.get_event_all_filters(search_dict))

    return {'concerts': artists_with_shows(concerts)}


if __name__ == '__main__':
    # Test the HTTP endpoints here
    # print(get_all_concerts_test({'playlist_id': '6lrx56m5B3afuYuCKdf2i9', 'city': 'Toronto'}))
    print(get_concerts_filtered_test({'playlist_id': '6lrx56m5B3afuYuCKdf2i9', 'city': 'Toronto'}))
