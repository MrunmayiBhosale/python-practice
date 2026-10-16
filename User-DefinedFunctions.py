#User-Defined Functions

def calculate_total(marks):
    return sum(marks)

def calculate_percentage(total):
    return total/5

def calculate_grade(percentage):
    if percentage >= 75:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 35:
        return "C"
    else:
        return "F"

def display_result(name,marks):
    total=calculate_total(marks)
    percentage=calculate_percentage(total)
    grade=calculate_grade(percentage)

    print("\nStudent Name:",name)
    print("Total Marks:", total)
    print("Percentage:",round(percentage, 1),"%")
    print("Grade:",grade)

    if percentage>=35:
        print("Result: Pass")
    else:
        print("Result:Fail")

name=input("Student Name:")

marks=[]
subjects=["Python","DS","Java","AWS","CPP"]

for subject in subjects:
    m=int(input(subject+":"))
    marks.append(m)

display_result(name,marks)
