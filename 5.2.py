largest = None
smallest = None
list = []
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        iput = int(num)
        list.append(iput)
    except:
        print ("Invalid input")

for i in list:
    if largest == None:
        largest = i
    elif i > largest:
        largest = i

for i in list:
    if smallest == None:
        smallest = i
    elif i < smallest:
        smallest = i

print("Maximum is", largest)
print("Minimum is", smallest)
