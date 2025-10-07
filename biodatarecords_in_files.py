import csv
import datetime

date = input("Enter date(dd/mm/yyyy) and time(hh:mm)")
name = input("Enter your name: ")
DOB = input("Enter your date of birth in dd/mm/yyyy: ")
bestfood = input("Enter your best food: ")
favcolor = input("Enter your favorite color: ")
shortbio = input("Enter a short biography about you: ")


csvfile = open(f"{date}.csv", "w")
csv_writer = csv.writer(csvfile)
csv_writer.writerow(["Full_Name", "Date of birth", "Best food", "Favorite Color", "Short Bio"])
csv_writer.writerow([name, DOB, bestfood, favcolor, shortbio])
print(f"The details have been registered")
yn = input("Do you want to add another record(yes/no)")
while yn.strip().lower() == "yes":
    name = input("Enter your name: ")
    DOB = input("Enter your date of birth in dd/mm/yyyy: ")
    bestfood = input("Enter your best food: ")
    favcolor = input("Enter your favorite color: ")
    shortbio = input("Enter a short biography about you: ")

    csv_writer.writerow([name, DOB, bestfood, favcolor, shortbio])
    print(f"The details have been registered")
    yn = input("Do you want to add another record(yes/no)")

csvfile.close()