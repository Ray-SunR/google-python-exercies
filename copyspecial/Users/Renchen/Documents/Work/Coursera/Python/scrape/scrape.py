from bs4 import BeautifulSoup
import urllib
 
content = urllib.urlopen("http://www.qq.com").read();
soup = BeautifulSoup(content);

tags = soup('a');
for tag in tags:
    print tag.get('href')
