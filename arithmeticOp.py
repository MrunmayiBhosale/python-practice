num1=int(input("enter first number"))

num2=int(input("enter second number"))

print("1. Addition (+)")

print("2. Subtraction (-)")

print("3. Multiplication (*)")

print("4. Division (/)")

choice=int(input("enter your choice"))

if choice==1:
    print(num1+num2)

elif choice==2:
    print(num1-num2)

if choice==1:
    print(num1+num2)

elif choice==2:
    print(num1-num2)

elif choice==3:
    print(num1*num2)

elif choice==4:
    print(num1/num2)

else:
    print("Enter a valid choice")