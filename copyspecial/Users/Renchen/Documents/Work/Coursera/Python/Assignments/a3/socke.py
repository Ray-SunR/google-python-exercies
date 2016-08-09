import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mysock.connect(('www.meteor.com', 80))

mysock.send('GET https://install.meteor.com/ \n\n')

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print data
mysock.close()

import urllib
response = urllib.urlopen("https://install.meteor.com/")
print response.read()