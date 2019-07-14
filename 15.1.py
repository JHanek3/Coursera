#read json from that url using urlib and then parse
#extract comment counts and sum the numbers

import urllib.request as ur
import json

url = input("Enter the url:")
if len(url) < 1: url = " http://py4e-data.dr-chuck.net/comments_42.json"

data = ur.urlopen(url).read().decode('utf-8')
info = json.loads(data)
print ("Succesful retrieval", len(data), "characters")

sum = 0

for comment in info["comments"]:
    sum += int(comment["count"])

print ("Sum:" , sum)
