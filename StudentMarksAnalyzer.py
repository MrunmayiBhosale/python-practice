marks=[79,67,60,90,86,72,83,77,43,66,87,93]

print("\nStudent Marks Analyzer\n")

print("1. Find how many students got a particular mark")
print("2. Check whether any student scored more than 90")
print("3. Calculate Total marks")
print("4. Display marks in ascending order")
print("5. Display total number of students")
print("6. Display highest and lowest marks")
print("7. Check whether all students scored atleast 35")

ch=int(input("\nEnter your choice:"))

if ch==1:
    mark=int(input("Enter particular marks:"))
    count=marks.count(mark)
    print("Number of students who scored:",mark,"=",count)

elif ch==2:
    if any(mark>90 for mark in marks):
        print("Yes,some students marks exceed 90")
    else:
        print("No,some students marks exceed 90")

elif ch==3:
    total=sum(marks)
    print("Total marks:",total)

elif ch==4:
    marks.sort()
    print("Marks in ascending order:",marks)

elif ch==5:
    print("Total number of students:",len(marks))

elif ch==6:
    print("Highest marks:",max(marks))
    print("Lowest marks:",min(marks))

elif ch==7:
    if all(mark>=35 for mark in marks):
        print("Yes,All students have scored at least 35")
    else:
        print("No,Some students have scored less than 35")

else:
    print("Invalid choice")