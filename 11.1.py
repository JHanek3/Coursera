import re

name = input("Enter file:")
if len(name) < 1 : name = "SampleData.txt"
#Auto run SampleData.txt
handle = open(name, 'r')
#Open the file in read only

result = 0
for line in handle.readlines():
#Iterate through the readlines

    for value in re.findall('[0-9]+', line):
    #use findall to find integers in the line and then add them below
        result += int(value)
print(result)
