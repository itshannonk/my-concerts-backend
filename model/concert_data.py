"""
All the ticketmaster stuff will be handled here.
"""
import ticketpy, json
from geopy.geocoders import Nominatim
import ssl
import certifi
import geopy.geocoders

# Initialize ticketmaster client
API_KEY = 'k2zkHLSGtq9fYAsPhysiijSpxn3GGkNh'
TM_CLIENT = ticketpy.ApiClient(API_KEY)

# Initialize geolocation
ctx = ssl.create_default_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx


def get_event_keyword(keyword: str) -> json:
    """ Search for keyword in ticketmaster events.

    :param keyword: The keyword that will be search for in the events.
    :return: A json object containing the search results.
    """
    pass


def get_event_location(location: str) -> json:
    """ Search for an event based on location.

    :param location: The location that will be searched for.
    :return: A json object containing the search results.
    """
    pass


def get_event_key_loc(keyword: str, location: str) -> json:
    """

    :param keyword: The keyword that will be search for in the events.
    :param location: The location that will be searched for.
    :return: A json object containing the search results.
    """
    pass


if __name__ == '__main__':
    pass
