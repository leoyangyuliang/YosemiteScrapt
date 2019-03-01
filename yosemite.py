from requests_html import HTMLSession
import json
from pprint import pprint

def checkCampsite(campsiteID):
    session = HTMLSession()
    march_URL = 'https://www.recreation.gov/api/camps/availability/campground/' + campsiteID + '/month?start_date=2019-03-01T00%3A00%3A00.000Z'
    march = session.get(march_URL)
    april_URL = 'https://www.recreation.gov/api/camps/availability/campground/' + campsiteID + '/month?start_date=2019-04-01T00%3A00%3A00.000Z'
    april = session.get(april_URL)
    april_dates = ['2019-04-01T00:00:00Z','2019-04-02T00:00:00Z','2019-04-03T00:00:00Z','2019-04-04T00:00:00Z','2019-04-05T00:00:00Z','2019-04-06T00:00:00Z']
    availableSites = []

    if campsiteID != '232450':
        for campsites in march.json()['campsites']:
            if march.json()['campsites'][campsites]['availabilities']['2019-03-30T00:00:00Z'] == 'Available' or march.json()['campsites'][campsites]['availabilities']['2019-03-31T00:00:00Z'] == 'Available':
    #             pprint(march.json()['campsites'][campsites]['site'])
    #             print(march.json()['campsites'][campsites]['availabilities']['2019-03-30T00:00:00Z'])
                availableSites.append({'date':'march', 'site':march.json()['campsites'][campsites]['site']})
    for campsites_april in april.json()['campsites']:
        for date in april_dates:
            if date in april.json()['campsites'][campsites_april]['availabilities']:
                if april.json()['campsites'][campsites_april]['availabilities'][date] == 'Available':
                    availableSites.append({'date': date, 'site':april.json()['campsites'][campsites_april]['site']})

    return availableSites

while(True):
    print("Searching...")
    print('-------------------------------------------')
    upperPines = checkCampsite('232447')
    print("Upper Pines: {}" .format(upperPines) )
    northPines = checkCampsite('232449')
    print("North Pines: {}" .format(northPines))
    shakesslough = checkCampsite('233067')
    print("shakes slough: {}" .format(shakesslough))
    lowerPines = checkCampsite('232450')
    print("lower Pines: {}" .format(lowerPines))
    if len(upperPines)>0:
        gmaill.send_email("Upper Pines", upperPines)
    elif len(northPines)>0:
        gmaill.send_email("North Pines", northPines)
    elif len(lowerPines)>0:
        gmaill.send_email("Lower Pines", lowerPines)
    elif len(shakesslough)>0:
        gmaill.send_email("shakesslough", shakesslough)
    
