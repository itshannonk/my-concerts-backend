"""
This will be the file containing my cloud functions.
"""
from flask import Request


def get_all_concerts(request: Request):
    """ Return a list of all concerts in the playlist with the given id.

    :param request: flask.Request object.
    :return: A json object containing the concerts of all artists in the playlist.
    """
    playlist_id = request.args['playlist_id']
    location = request.args['location']
    pass


def get_concert(request: Request):
    """ Return all the business owners' unique ids.

    :param request: flask.Request object.
    :return: Comma separated string of unique ids.
    """
    pass
