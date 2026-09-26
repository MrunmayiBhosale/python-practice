marks=[79,67,60,90,86,72,83,77,43,66,87,93]

print("\nStudent Marks Analyzer\n")

print("1. Find how many students got a particular mark")
print("2. Check whether any student scored more than 90")
print("3. Calculate Total marks")
print("4. Display marks in ascending order")

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



else:
    print("Invalid choice")