import urllib
from bs4 import BeautifulSoup

URL = input("Enter the URL:") #Enter main URL
link_line = int(input("Enter position:")) - 1 #The position of link relative to first link
count = int(input("Enter count:")) #The number of times to be repeated

while count >= 0:
    html = urllib.urlopen(URL).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    print (URL)
    URL = tags[link_line].get("href", None)
    count = count - 1
