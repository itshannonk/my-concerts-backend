"""
This is the file in which we will test the ticketmaster API.
"""
import ticketpy, json
import requests
API_KEY = 'k2zkHLSGtq9fYAsPhysiijSpxn3GGkNh'

URL = 'http://app.ticketmaster.com//discovery/v2/events.json?' \
      'keyword=Dijon&apikey=k2zkHLSGtq9fYAsPhysiijSpxn3GGkNh&' \
      'localStartDateTime=2020-01-30T00:00:00,2020-02-28T23:59:00'
      # 'city=Toronto&'
                         # 2020-07-08T14:00:00,2020-08-01T14:00:00
r = requests.get(URL)
data = r.json()
print(data)
"""tm_client = ticketpy.ApiClient(API_KEY)

pages = tm_client.events.find(
    country_code='CA',
    start_date_time='2020-01-19T20:00:00Z',
    end_date_time='2020-02-21T20:00:00Z',
    keyword='Dijon'
)

# Convert pages to json object
print(json.dumps(pages.__dict__, default=lambda o: o.__dict__, check_circular=False))

# print(pages.json)
for page in pages:
    # print(page)
    for event in page:
        print('EVENT --------------------------------------------')
        print(event)
        print('VENUE --------------------------------------------')
        print(event.venues)
        print('CLASSIFICATIONS ----------------------------------')
        print(event.classifications)
        print('')"""

