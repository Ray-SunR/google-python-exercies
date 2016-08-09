import urllib,json

API_KEY = 'AIzaSyAGdXGRCqMbHWfYfr8a64UPV9nF06_usag'
service_url = 'https://maps.googleapis.com/maps/api/geocode/'

#url = service_url + 'json?' + urllib.urlencode({'address': 'BITS Pilani', 'key': API_KEY})
#link = urllib.urlopen(url)
#print(link.read())

service_url_2 = 'http://python-data.dr-chuck.net/geojson?'
while True:
    address = raw_input('Enter a location: ')
    if len(address) == 0:
        break
    else:
        url2 = service_url_2 + urllib.urlencode({'sensor': 'false', 'address': address})
        try:link = urllib.urlopen(url2)
        except:link = None
        if link is None:
            continue
        elif link.getcode() == 200:
            ret = json.loads(link.read())
            if len(ret['results']):
                print(ret['results'][0]['place_id'])
        else:
            continue