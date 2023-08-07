class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def get_account_info(self):
        return f"Account Number: {self.account_number}\nAccount Holder: {self.account_holder}\nBalance: ${self.balance:.2f}"


def main():
    accounts = {}  # Dictionary to store account_number as the key and BankAccount object as the value

    while True:
        print("\nWelcome to the Banking System")
        print("1. Create New Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        choice = int(input("Enter your choice (1-5): "))

        if choice == 1:
            account_number = input("Enter Account Number: ")
            account_holder = input("Enter Account Holder Name: ")
            initial_balance = float(input("Enter Initial Balance: "))
            account = BankAccount(account_number, account_holder, initial_balance)
            accounts[account_number] = account
            print("Account Created Successfully!")

        elif choice == 2:
            account_number = input("Enter Account Number: ")
            if account_number in accounts:
                amount = float(input("Enter Deposit Amount: "))
                if accounts[account_number].deposit(amount):
                    print("Deposit Successful.")
                else:
                    print("Invalid Deposit Amount.")
            else:
                print("Account not found.")

        elif choice == 3:
            account_number = input("Enter Account Number: ")
            if account_number in accounts:
                amount = float(input("Enter Withdrawal Amount: "))
                if accounts[account_number].withdraw(amount):
                    print("Withdrawal Successful.")
                else:
                    print("Invalid Withdrawal Amount or Insufficient Balance.")
            else:
                print("Account not found.")

        elif choice == 4:
            account_number = input("Enter Account Number: ")
            if account_number in accounts:
                print(accounts[account_number].get_account_info())
            else:
                print("Account not found.")

        elif choice == 5:
            print("Exiting the Banking System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
