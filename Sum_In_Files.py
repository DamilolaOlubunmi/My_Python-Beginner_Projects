x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
sum = x + y
file = open("../sum_output.txt", "w")
file.write(f"Input 1 : {x}\n")
file.write(f"Input 2 : {y}\n")
file.write(f"Sum : {sum}\n")

file.close()
print("The sum has been written to file - sum_output.txt")