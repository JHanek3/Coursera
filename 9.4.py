name = input("Enter file:")
handle = open(name)

book = dict()

for line in handle:
    x = line.split()
    if "From" in x:
        sender = x[1]
        if sender not in book:
            book[sender] = 1
        else:
            book[sender] = book[sender] + 1

final_sender = None
final_count = None
for sender,count in book.items():
    if final_count is None or count > final_count:
        final_sender = sender
        final_count = count
print (final_sender, final_count)
