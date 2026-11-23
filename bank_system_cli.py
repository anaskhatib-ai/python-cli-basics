bal = 1000 # initial

def deposit(bal,amount):
    return amount + bal

def withdrawl(bal,amount):
        return bal - amount

def checkbalance(bal):
    return bal

# ----------------------
while True:
    print("\n ____MENU_____\n 1. deposit\n 2. withdrawl\n 3. checkbalance\n 4. Exit \n")

    choice = input("Enter number, what to do:").strip()

    if not choice.isdigit():
        print("Invalid choice, enter number")
        continue
    choice = int(choice)

    if choice == 1:

        amount = input("Enter amount to deposit:").strip()

        if not amount.isdigit():
            print("Invalid amount")
            continue
        
        amount = int(amount)

        if amount <= 0:
            print("Amount should be positive")
            continue
        
        
        bal = deposit(bal,amount)
        print(amount,"rs deposited successfully!")
        print("New balance:", bal)

    elif choice == 2:
        amount = input("Enter amount to withdraw:",).strip()

        if not amount.isdigit():
            print("invalid amount")
            continue
        
        amount = int(amount)
        
        if amount <= 0:
            print("Amount should be positive")
            continue

        elif amount > bal:
            print("insuffitiant balance")
            continue
                
        bal = withdrawl(bal,amount)
        print(amount,"rs withdrawled successfully!")
        print("New balance:",bal)

    elif choice == 3:
        print("Your current balance is:",checkbalance(bal))

    elif choice == 4:
        print("Good bye!")
        break
    
    else:
        print("Invalid choice!")