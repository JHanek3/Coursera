import urllib.request
from bs4 import BeautifulSoup

URL = input("Enter the URL:")
if len(URL) < 1: URL = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"

position = int(input("Enter position:")) - 1
count = int(input("Enter Count:"))

while count >= 0:
    html = urllib.request.urlopen(URL).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    print (URL)
    URL = tags[position].get("href",None)
    count = count - 1
