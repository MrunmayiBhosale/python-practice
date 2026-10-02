print("---HOSPITAL PATIENT MANAGEMENT SYSTEM---\n")

patients=["Priya","Riya","Diya","Amit","Ajit"]
print("Patients name:",patients)

new_patients=input("\nEnter patients name:")
patients.append(new_patients)
print("After adding new patients:",patients)

eme_patients=input("\nEnter emergency patients name:")
patients.insert(0,eme_patients)
print("After adding emergency patients:",patients)

discharge_patients=input("\nEnter discharged patients name:")
patients.remove(discharge_patients)
print("After removing discharged patients:",patients)

search_patients=input("\nEnter patients name to search:")
if search_patients in patients:
    print("patients found")
else:
    print("patients not found")
find_patients=input("\nEnter patients name to find it's position:")

print("patients position is:",patients.index(find_patients))
print("first five patients:",patients[:5])
print("Total number of patients:",len(patients))