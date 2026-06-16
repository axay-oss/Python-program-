balance = 10000

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current Balance =", balance)

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print("Amount Deposited Successfully!")
        print("New Balance =", balance)

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= balance:
            balance -= amount
            print("Amount Withdrawn Successfully!")
            print("Remaining Balance =", balance)
        else:
            print("Insufficient Balance!")

    elif choice == 4:
        print("Thank You for Using ATM")
        break

    else:
        print("Invalid Choice!")