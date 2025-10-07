name = input("Enter your name: ")
DOB = input("Enter your date of birth in dd/mm/yyyy: ")
bestfood = input("Enter your best food: ")
favcolor = input("Enter your favorite color: ")
shortbio = input("Enter a short biography about you: ")

me = open(f"{name}.txt", "w")

me.write(f"My name is {name} and I was born on {DOB}.My favorite color is {favcolor}.")
me.write(f"\n {shortbio}")

me.close()
print(f"The details have been saved in {name}.txt")
