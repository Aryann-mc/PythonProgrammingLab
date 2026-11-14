#Bank account system using OOP
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount:.2f}.")
        else:
            print("Enter an amount greater than zero.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Enter an amount greater than zero.")
        elif amount > self.balance:
            print("Not enough money in the account.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount:.2f}.")

    def show_balance(self):
        print(f"{self.owner}'s balance: {self.balance:.2f}")


name = input("Account owner's name: ")
account = BankAccount(name)

while True:
    print("\n1. Deposit\n2. Withdraw\n3. Show balance\n4. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        try:
            account.deposit(float(input("Amount to deposit: ")))
        except ValueError:
            print("Please enter a valid number.")
    elif choice == "2":
        try:
            account.withdraw(float(input("Amount to withdraw: ")))
        except ValueError:
            print("Please enter a valid number.")
    elif choice == "3":
        account.show_balance()
    elif choice == "4":
        break
    else:
        print("Please enter 1, 2, 3, or 4.")
