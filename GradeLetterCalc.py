print("Grade letter Analyser")
score = int(input("Input your score for the course: "))

if score >= 70:
    if score > 100:
        print("Invalid Input")
    else:
        print("A")
else:
    if score >= 59:
        print("B")
    else:
        if score >= 49:
            print("C")
        else:
            if score >= 45:
                print("D")
            else:
                if score < 45:
                    print("F")
                else:
                    print("Invalid input")
input(" ")
