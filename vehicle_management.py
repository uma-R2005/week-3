class Vehicle:
    def __init__(self, reg_no, brand, model):
        self.reg_no, self.brand, self.model = reg_no, brand, model
    def get_info(self):
        return f"{self.reg_no} | {self.brand} {self.model}"

class Car(Vehicle):
    def __init__(self, reg_no, brand, model, seats):
        super().__init__(reg_no, brand, model)
        self.seats = seats
    def get_info(self):
        return super().get_info() + f" | Car - Seats: {self.seats}"

class Truck(Vehicle):
    def __init__(self, reg_no, brand, model, capacity):
        super().__init__(reg_no, brand, model)
        self.capacity = capacity
    def get_info(self):
        return super().get_info() + f" | Truck - Capacity: {self.capacity} tons"

class Motorcycle(Vehicle):
    def __init__(self, reg_no, brand, model, engine_cc):
        super().__init__(reg_no, brand, model)
        self.engine_cc = engine_cc
    def get_info(self):
        return super().get_info() + f" | Motorcycle - Engine: {self.engine_cc}cc"

vehicles = [
    Car("KA01AB1234", "Toyota", "Corolla", "5"),
    Truck("KA02CD5678", "Volvo", "FH16", "20"),
    Motorcycle("KA03EF9012", "Yamaha", "R15", "150"),
]

while True:
    cmd = input("\nOptions: add_car, add_truck, add_motorcycle, list, exit\n> ").strip()
    if cmd == "add_car":
        r,b,m,s = input("Reg No: "), input("Brand: "), input("Model: "), input("Seats: ")
        vehicles.append(Car(r,b,m,s))
        print("Car added.")
    elif cmd == "add_truck":
        r,b,m,c = input("Reg No: "), input("Brand: "), input("Model: "), input("Capacity (tons): ")
        vehicles.append(Truck(r,b,m,c))
        print("Truck added.")
    elif cmd == "add_motorcycle":
        r,b,m,e = input("Reg No: "), input("Brand: "), input("Model: "), input("Engine CC: ")
        vehicles.append(Motorcycle(r,b,m,e))
        print("Motorcycle added.")
    elif cmd == "list":
        if not vehicles:
            print("No vehicles added.")
        else:
            for v in vehicles:
                print(v.get_info())
    elif cmd == "exit":
        print("Goodbye!")
        break
    else:
        print("Invalid command.")
