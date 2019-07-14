def computepay(h,r):
    x = float(h)
    y = float(r)
    final_pay = 0
    if x <= 40:
        final_pay = (x * y)

    elif x > 40:
        b = x - 40
        final_pay = ((1.5 * y * b) + (40 * y))

    else:
        ("Please enter a valid number.")
    return print(final_pay)
computepay(input("Enter Hours: "), input("Enter Rate: "))
