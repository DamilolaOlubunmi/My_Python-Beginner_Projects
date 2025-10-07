
grade_points = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2,
    "F" : 0,
}
courses = [
    ("CSC 241", 3),
    ("CIT 221", 0),
    ("CSC 242", 2),
    ("COS 221", 3),
    ("DLD 121", 0),
    ("DTS 224", 3),
    ("ENT 221", 1),
    ("INS 224", 3),
    ("IFT 222", 2),
    ("TMC 221", 1)
]
name = input("Type in your full name: ")

total_points = 0
total_units = 0
course_record = []

for course, unit in courses:
    grade = input(f"Enter grade for {course}: ").upper().strip()
    grade_point = grade_points.get(grade, -1)

    course_record.append((course, grade, unit))
    total_units += unit
    total_points += grade_point * unit
    gpa = total_points/total_units
    continue

print(f"\n\nYour total_units is: {total_units: .2f}")
print(f"Your total_points is: {total_points: .2f}")
print(f"Your gpa is: {gpa: .2f}")



# print("Welcome to the GPA calculator!!!!!!")
# # no_of_courses = int(input(f"\n How many courses do you do? "))
# # for i in range(no_of_courses):
# while True:
#     course = input("Enter course name(or type 'done' to finish)")
#     if course.lower() == 'done':
#         break
#
#     units = float(input(f"Enter number of units for {course}: "))
#
#     grade_points = grade_scale[grade]
#     total_points += grade_points * units
#     total_units += units
#     continue
#
#     # grade_points = grade_scale[grade]
#     # total_points += grade_points * units
#     # total_units += units
#
#     gpa = total_points/ total_units
#     print(f"\n Your GPA is: {gpa: .2f}")
