import functools

def requires_role(role):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(user, *args):
            if user.get("role") != role:
                return f"Access denied: Requires {role}"
            return func(user, *args)
        return wrapper
    return decorator

def log_action(func):
    @functools.wraps(func)
    def wrapper(user, *args):
        print(f"User {user['name']} ({user.get('role')}) performed {func.__name__}")
        return func(user, *args)
    return wrapper

@requires_role("admin")
@log_action
def update_price(user, product, price):
    return f"Price of '{product}' updated to ${price:.2f}."

@requires_role("customer")
@log_action
def place_order(user, product, qty):
    return f"{user['name']} placed order for {qty} unit(s) of '{product}'."

def main():
    name = input("Name: ").strip()
    role = input("Role (admin/customer): ").strip().lower()
    if role not in ("admin", "customer"):
        print("Invalid role!"); return
    user = {"name": name, "role": role}
    while True:
        if role == "admin":
            choice = input("\n1.Update Price\n2.Exit\nChoose: ").strip()
            if choice == "1":
                p = input("Product: ").strip()
                try: price = float(input("New price: "))
                except: print("Invalid price."); continue
                print(update_price(user, p, price))
            elif choice == "2": break
            else: print("Invalid choice.")
        else:
            choice = input("\n1.Place Order\n2.Exit\nChoose: ").strip()
            if choice == "1":
                p = input("Product: ").strip()
                q = input("Quantity: ").strip()
                if not q.isdigit() or int(q) < 1:
                    print("Invalid quantity."); continue
                print(place_order(user, p, int(q)))
            elif choice == "2": break
            else: print("Invalid choice.")
    print("Goodbye!")

if __name__ == "__main__":
    main()
