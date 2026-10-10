#Dictionary

employee={
    "Mrunmayi":45000,
    "Priya":50000,
    "Siya":42000,
    "Diya":55000,
    "Ram":48000
}

print("All Employees Record:")
print(employee)
print("\nNumber of Employees:",len(employee))

print("\nEmployee Names:")
print(employee.keys())

print("\nEmployee Salaries:")
print(employee.values())

print("\n Employee-Salary Pairs:")
print(employee.items())

name="Mrunmayi"
print("\nSalary of",name,":",employee.get(name))

employee.update({"Priya":50000})
print("\nAfter Updating Sham's Salary:")
print(employee)

employee.update({"Siya":42000})
print("\nAfter adding Siya:")
print(employee)

employee.pop("Ram")
print("\nAfter removing Ram:")
print(employee)

print("\nEmployee name in alphabetical order:")
print(sorted(employee.keys()))

print("\nData Type of Dictionary:")
print(type(employee))