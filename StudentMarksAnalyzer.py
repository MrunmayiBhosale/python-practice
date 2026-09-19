marks=[79,67,60,90,86,72,83,77,43,66,87,93]

print("\nStudent Marks Analyzer\n")

print("1. Find how many students got a particular mark")

ch=int(input("\nEnter your choice:"))

if ch==1:
    mark=int(input("Enter particular marks:"))
    count=marks.count(mark)
    print("Number of students who scored:",mark,"=",count)

else:
    print("Invalid choice")