score = input("Enter Score: ")
score_grade = float(score)

if 1 > score_grade >= .9:
    print ("A")

elif .9 > score_grade >= .8:
    print("B")

elif .8 > score_grade >= .7:
    print("C")

elif .7 > score_grade >= .6:
    print("D")

elif .6 > score_grade > 0:
    print("F")

else:
    print("Please enter a number between 0 and 1.")
    quit()
