
student=(101,"Mrunmayi","B.Tech CSE")
subjects=("Python","RDBMS","DS","Physics","Maths")
marks=(63,45,56,43,77)

print("\n----Student Result Management System----")
print("1.Display student details")
print("2.Display subject-wise marks")
print("3.Perform Tuple Slicing")
print("4.Check subject membership")
print("5.Count duplicate marks")
print("6.calculate Total marks")
print("7.Find Highest mark")
print("8.Find lowest mark")
print("9.Display sorted marks")
print("10.Exit")

choice=int(input("Enter your choice:"))
if choice==1:
    print("\nStudent Details")
    print("Roll No:", student[0])
    print("Name:", student[1])
    print("Marks:", student[2])

elif choice==2:
    print("\nSubject-wise Marks")
    for i in range(len(student)):
        print(student[i], ":", marks[i])

elif choice==3:
    print("\nTuple Slicing")
    print("First 3 subjects:", subjects[:3])
    print("Find 3 Marks:", marks[:3])

elif choice==4:
    subject = input("Enter subject to search:")
    if subject in subjects:
        print(subject, "is present in tuple")
    else:
        print(subject, "is not present in tuple")

elif choice==5:
    mark = int(input("Enter mark to count:"))
    print("Count of", mark, "=", marks.count(mark))

elif choice==6:
    print("Total marks:",sum(marks))

elif choice==7:
    print("Highest mark:",max(marks))

elif choice==8:
    print("Lowest mark:",min(marks))

elif choice==9:
    print("Sorted marks:",tuple(sorted(marks)))

elif choice==10:
    print("Exit")
    
else:
    print("Invalid Choice")