from student_package.marks import calculate_total, calculate_percentage
from student_package.grade import calculate_grade

name = input("Enter Student Name: ")

print("Enter marks of 5 subjects:")
subjects = ["Python", "RDBMS", "Java", "OS", "CNC"]
marks = []

for subject in subjects:
    mark = int(input(subject + ": "))
    marks.append(mark)

total = calculate_total(marks)
percentage = calculate_percentage(total)
grade = calculate_grade(percentage)

print("\n------ STUDENT RESULT ------")
print("Name       :", name)
print("Total      :", total)
print("Percentage :", str(round(percentage, 2)) + "%")
print("Grade      :", grade)