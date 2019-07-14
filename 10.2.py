name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counter = dict()
lst = list()

for line in handle:
    x = line.split()
    if "From" in x:
        y = str(x[5])
        z = (y[0:2])

        counter[z] = counter.get(z, 0) + 1

for key, val in counter.items():
    newtup = (key,val)
    lst.append(newtup)

lst = sorted(lst)

for val, key in lst:
    print( val, key)
