import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input("Enter the URL:")
if len(url) < 1: url = "http://py4e-data.dr-chuck.net/comments_42.xml"

xml = urllib.request.urlopen(url).read()
print ("Retrieved: " + str(len(xml)) + " characters")

tree = ET.fromstring(xml)
counts = tree.findall('.//count')

total = 0

for count in counts:
    total += int(count.text)


print ("Sum: " + str(total))
