fname = input("Enter file name: ")

fh = open(fname)
count = 0
for line in fh:
    x = line.split()
    if "From" in x:
        print(x[1])
        count = count + 1

print("There were", count, "lines in the file with From as the first word")
