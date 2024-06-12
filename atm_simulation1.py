class ATM:
    def __init__(self, balance=0):
        self.balance = balance
        self.transaction_history = []

    def check_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount:.2f}")
            print(f"${amount:.2f} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawn: ${amount:.2f}")
            print(f"${amount:.2f} withdrawn successfully.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount.")

    def transfer(self, amount, recipient_account):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            recipient_account.balance += amount
            self.transaction_history.append(f"Transferred: ${amount:.2f} to {recipient_account}")
            recipient_account.transaction_history.append(f"Received: ${amount:.2f} from {self}")
            print(f"${amount:.2f} transferred successfully.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            print("Invalid transfer amount.")

    def view_transaction_history(self):
        if self.transaction_history:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("No transactions yet.")

def main():
    print("Welcome to the ATM!")
    atm = ATM(1000)  # Initial balance for the ATM
    while True:
        print("\nPlease select an option:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. View Transaction History")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            amount = float(input("Enter the amount to deposit: $"))
            atm.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter the amount to withdraw: $"))
            atm.withdraw(amount)
        elif choice == '4':
            amount = float(input("Enter the amount to transfer: $"))
            recipient_account = ATM()  # For simplicity, we create a new account here
            atm.transfer(amount, recipient_account)
        elif choice == '5':
            atm.view_transaction_history()
        elif choice == '6':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
