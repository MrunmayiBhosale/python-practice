balance=10000

print("--ATM Menu--\n")
print("1. Balance Inquiry")
print("2. Deposit Money")
print("3. Withdraw Money\n")

choice=int(input("Enter your choice:"))

if choice==1:
    print("Current balance:",balance)
elif choice==2:
    amount=float(input("Enter Deposit amount:"))
    if amount>0:
        balance+=amount
        print("Amount deposited successfully")
        print("Updated balance:",balance)
    else:
        print("Invalid amount entered")
elif choice==3:
    amount=float(input("Enter withdraw amount:"))
    if amount>0:
        if amount<=balance:
            balance-=amount
            print("Amount withdrawn successfully")
            print("Updated balance:",balance)
        else:
            print("Insufficient balance")
    else:
        print("Invalid amount entered")
else:
 print("Invalid choice")