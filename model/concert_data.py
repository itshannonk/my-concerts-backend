"""
All the ticketmaster stuff will be handled here.
"""
import requests, json
URL = 'http://app.ticketmaster.com//discovery/v2/events.json?'
API_KEY = 'k2zkHLSGtq9fYAsPhysiijSpxn3GGkNh'
# A tuple containing the valid concert filter
FILTERS = ('id', 'keyword', 'locale', 'localStartDateTime', 'sort', 'city')


def get_event_keyword(keyword: str) -> json:
    """ Search for keyword in ticketmaster events.

    :param keyword: The keyword that will be search for in the events.
    :return: A json object containing the search results.
    """
    url = URL + "keyword={}&apikey={}".format(keyword, API_KEY)
    return requests.get(url).json()


def get_event_city(city: str) -> json:
    """ Search for an event based on location.

    :param city: The location that will be searched for.
    :return: A json object containing the search results.
    """
    url = URL + "city={}&apikey={}".format(city, API_KEY)
    return requests.get(url).json()


def get_event_key_city(keyword: str, city: str) -> json:
    """ Search for an event based on key word and location.

    :param keyword: The keyword that will be search for in the events.
    :param city: The location that will be searched for.
    :return: A json object containing the search results.
    """
    url = URL + "keyword={}&city={}&apikey={}".format(keyword, city, API_KEY)
    return requests.get(url).json()


def get_event_all_filters(filters: dict) -> json:
    """ Return an event that matches all filters in filters.

    :param filters: flask.Request.args filter response
    :return: A json object containing the search results.
    """
    url = URL + 'apikey=' + API_KEY  # Initialize URL for query
    for c_filter in filters:
        if c_filter in FILTERS:  # Make sure the filter is valid
            url = url + '&' + c_filter + '=' + filters[c_filter]
    return requests.get(url).json()


if __name__ == '__main__':
    # print(get_event_key_city('Dijon', 'Toronto'))
    # print(get_event_all_filters({'bobo': 'hihi',
    #                              'keyword': 'Dijon', 'city': 'Toronto'}))
    pass
