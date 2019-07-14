# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
value = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    digit = (line[20:])
    fvalue = float(digit)
    value = fvalue + value
    final = round(value / count, 12)

print ("Average spam confidence:", final)
