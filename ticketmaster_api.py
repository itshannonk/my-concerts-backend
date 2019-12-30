"""
This is the file in which we will test the ticketmaster API.
"""
import ticketpy
API_KEY = 'k2zkHLSGtq9fYAsPhysiijSpxn3GGkNh'

tm_client = ticketpy.ApiClient(API_KEY)

pages = tm_client.events.find(
    country_code='CA',
    start_date_time='2020-01-19T20:00:00Z',
    end_date_time='2020-02-21T20:00:00Z',
    keyword='Dijon'
)
for page in pages:
    # print(page)
    for event in page:
        print('EVENT --------------------------------------------')
        print(event)
        print('VENUE --------------------------------------------')
        print(event.venues)
        print('CLASSIFICATIONS ----------------------------------')
        print(event.classifications)
        print('')

