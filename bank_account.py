class BankAccount:
    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"✅ Deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("❌ Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("❌ Insufficient balance.")
        else:
            self.balance -= amount
            print(f"✅ Withdrew ₹{amount}. New balance: ₹{self.balance}")

    def check_balance(self):
        print(f"💰 Current balance: ₹{self.balance}")

    def calculate_interest(self, rate):
        interest = self.balance * (rate / 100)
        print(f"💸 Interest at {rate}% = ₹{interest:.2f}")
        return interest

    def show_account_info(self):
        print("\n🏦 Account Information:")
        print(f"👤 Name: {self.account_holder}")
        print(f"🔢 Account Number: {self.account_number}")
        self.check_balance()

# === Demo / Simulation ===
if __name__ == "__main__":
    # Create an account
    my_account = BankAccount("Ananya Sharma", "1234567890", 1000)

    # Use methods
    my_account.show_account_info()
    my_account.deposit(500)
    my_account.withdraw(200)
    my_account.calculate_interest(5)
    my_account.check_balance()
