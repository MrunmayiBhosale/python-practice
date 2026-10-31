import student_module

name = input("Enter Student Name: ")

print("Enter marks for 5 subjects:")
marks = []

for i in range(5):
    marks.append(int(input()))

total = student_module.calculate_total(marks)
percentage = student_module.calculate_percentage(total)
grade = student_module.calculate_grade(percentage)

print("\nStudent Result")
print("-------------------------")
print("Name       :", name)
print("Total      :", total)
print("Percentage :", str(round(percentage, 1)) + "%")
print("Grade      :", grade)