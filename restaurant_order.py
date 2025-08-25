class Order:
    def __init__(self, order_id, customer_name):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = []  # List of (item_name, price)
        self.total = 0.0

    def add_item(self, item_name, price):
        self.items.append((item_name, price))
        self.total += price
        print(f"➕ Added {item_name} for ₹{price:.2f} to order {self.order_id}")

    def remove_item(self, item_name):
        for i, (name, price) in enumerate(self.items):
            if name == item_name:
                self.total -= price
                del self.items[i]
                print(f"❌ Removed {item_name} from order {self.order_id}")
                return
        print(f"⚠️ Item {item_name} not found in order {self.order_id}")

    def view_order(self):
        print(f"\n🧾 Order ID: {self.order_id}")
        print(f"👤 Customer: {self.customer_name}")
        print("🍽️ Items:")
        for item, price in self.items:
            print(f"   - {item}: ₹{price:.2f}")
        print(f"💰 Total: ₹{self.total:.2f}")

    def checkout(self):
        if not self.items:
            print("⚠️ No items in the order to checkout.")
        else:
            print(f"✅ Order {self.order_id} completed. Total bill: ₹{self.total:.2f}")

# === Demo ===
if __name__ == "__main__":
    order1 = Order(101, "Ravi Kumar")

    order1.add_item("Paneer Butter Masala", 250.00)
    order1.add_item("Garlic Naan", 40.00)
    order1.view_order()

    order1.remove_item("Garlic Naan")
    order1.view_order()

    order1.checkout()
