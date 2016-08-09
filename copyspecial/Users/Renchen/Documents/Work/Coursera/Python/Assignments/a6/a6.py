__author__ = 'Renchen'
import urllib, json, sys

while True:
    url = raw_input('Enter a link: ')
    if len(url) == 0:
        break
    try:
        response = urllib.urlopen(url)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        continue
    if response.getcode() == 200:
        read = response.read()
        print('Successfully get response from url: ' + response.geturl())
        read_json = json.loads(read)
        ret = 0
        for item in read_json['comments']:
            ret += item['count']
        print('Sum: ' + str(ret))
    else:
        print('Error code: ' + response.getcode())
