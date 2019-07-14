text = "X-DSPAM-Confidence:    0.8475"
start = text.find("0")
finish = text.find("5")

value = text[start:finish + 1]

final = float(value)
print (final)
