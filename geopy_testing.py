from geopy.geocoders import Nominatim
import ssl
import certifi
import geopy.geocoders

ctx = ssl.create_default_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx

locator = Nominatim(user_agent="myGeocoder")
location = locator.geocode("Toronto")
print(location.address)
print((location.latitude, location.longitude))
