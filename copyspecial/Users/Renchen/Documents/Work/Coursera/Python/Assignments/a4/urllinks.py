# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter - ')
count = input('Count - ')
position = input('Position - ')
position = position - 1
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')
tag = ''
while count > 0:
	if position < len(tags):
		tag = tags[position]
		html = urllib.urlopen(tag['href']).read()
		soup = BeautifulSoup(html)
		tags = soup('a')
		count = count - 1
	else:
		print 'wrong input, posiiton exceeds the number of links'

print tag.contents[0]