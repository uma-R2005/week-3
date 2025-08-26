class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Insufficient funds.")

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.03):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest of ₹{interest:.2f} applied. New balance: ₹{self.balance:.2f}")

# -------- User Input Example --------
name = input("Enter account holder name: ")
initial_balance = float(input("Enter initial balance: "))
account = SavingsAccount(name, initial_balance)

while True:
    print("\n1.Deposit  2.Withdraw  3.Apply Interest  4.Show Balance  5.Exit")
    choice = input("Choose option: ")
    if choice == '1':
        amt = float(input("Enter deposit amount: "))
        account.deposit(amt)
    elif choice == '2':
        amt = float(input("Enter withdrawal amount: "))
        account.withdraw(amt)
    elif choice == '3':
        account.apply_interest()
    elif choice == '4':
        print(f"Current balance: ₹{account.balance:.2f}")
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid option.")
