import random, functools

def log(func):
    @functools.wraps(func)
    def wrapper(*a, **k):
        print(f"{func.__name__} called with {a[1:]}")
        r = func(*a, **k)
        print(f"Result: {r}")
        return r
    return wrapper

def requires_manager(func):
    @functools.wraps(func)
    def wrapper(self, *a, **k):
        if self.role != "manager":
            return "Access denied"
        return func(self, *a, **k)
    return wrapper

def handle_errors(func):
    @functools.wraps(func)
    def wrapper(*a, **k):
        try: return func(*a, **k)
        except Exception as e: return f"Error: {e}"
    return wrapper

class Bank:
    def __init__(self):
        self.accounts = {1:1000}
        self.role = "user"

    @log
    def deposit(self, acc, amt):
        if acc not in self.accounts or amt<=0: return "Invalid input"
        self.accounts[acc] += amt
        return f"Deposited {amt}"

    @requires_manager
    @handle_errors
    @log
    def approve_loan(self, loan_id):
        if random.random()<0.5: raise Exception("Failed approval")
        return f"Loan {loan_id} approved"

def main():
    bank = Bank()
    while True:
        role = input("Role (user/manager) or exit: ").strip().lower()
        if role == "exit": break
        if role not in ("user","manager"):
            print("Invalid role"); continue
        bank.role = role

        action = input("Action: deposit(1), approve loan(2), exit(3): ").strip()
        if action == "1":
            try:
                acc = int(input("Account #: "))
                amt = float(input("Amount: "))
                print(bank.deposit(acc, amt))
            except: print("Invalid input")
        elif action == "2":
            loan_id = input("Loan ID: ").strip()
            print(bank.approve_loan(loan_id))
        elif action == "3":
            print("Bye!"); break
        else:
            print("Invalid action")

if __name__=="__main__":
    main()
