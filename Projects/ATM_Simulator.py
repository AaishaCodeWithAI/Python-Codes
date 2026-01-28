def check_balance(balance):
    print(f"Your balance is: Rs. {balance}")


def deposit(balance):
    amount = float(input("Enter deposit amount: "))
    if amount > 0:
        balance += amount
        print("Deposit successful.")
    return balance


def withdraw(balance):
    amount = float(input("Enter withdrawal amount: "))
    if amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print("Withdrawal successful.")
    return balance


def main():
    balance = 1000

    while True:
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            check_balance(balance)
        elif choice == "2":
            balance = deposit(balance)
        elif choice == "3":
            balance = withdraw(balance)
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
