import urllib
import xml.etree.ElementTree as ET


while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(address)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    print data
    tree = ET.fromstring(data)


    counts = tree.findall('.//count')
    results = 0
    for count in counts:
        results += int(count.text)

    print results
