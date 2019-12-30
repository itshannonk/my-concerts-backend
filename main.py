"""
This will be the file containing my cloud functions.
"""
from flask import Request
from model import playlist_data, concert_data
import json


def get_all_concerts(request: Request):
    """ Return a list of all concerts in the playlist with the given id.

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
    """ Return all the business owners' unique ids.

    :param request: flask.Request object.
    :return: Comma separated string of unique ids.
    """
    concert_id = request.args['concert_id']
    pass


def artists_with_shows(concerts: json) -> list:
    """ Return a list containing artists with upcoming concerts

    :param concerts: A list containing info for all artists.
    :return: List containing concert info.
    """
    shows = []
    for concert in concerts:
        if concert['pages']['totalPages'] > 0:
            shows.append(concert)
    return shows
