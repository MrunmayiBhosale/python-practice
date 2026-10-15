#Python Built-in functions

marks=[]

for i in range(1,6):
    m=int(input("Enter marks of Student "+str(i)+":"))
    marks.append(m)

print("\nNumber of Students:",len(marks))

print("Highest Mark:",max(marks))

print("Lowest Mark:",min(marks))

print("Total Mark:",sum(marks))

print("Average Mark:",sum(marks)/len(marks))

print("Ascending Order:",sorted(marks))

print("Data Type:",type(marks))