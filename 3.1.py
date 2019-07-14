hrs = input("Enter Hours: ")
h = float(int(hrs))
rate = input("Enter Rate: ")
r = float(rate)
if h <= 40:
    print (h * r)
elif h > 40:
    x = h - 40
    print ((1.5 * r * x) + (40 * r))
else:
    ("Please enter a valid number.")
