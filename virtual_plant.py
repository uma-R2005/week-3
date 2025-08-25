import time
import random

class VirtualPlant:
    def __init__(self, name):
        self.name = name
        self.water_level = 5      # Max is 10
        self.sunlight = 5         # Max is 10
        self.growth = 0           # Increases over time
        self.alive = True

    def mood(self):
        if not self.alive:
            return "💀 Dead"
        if self.water_level >= 7 and self.sunlight >= 7:
            return "🌻 Thriving"
        elif self.water_level >= 4 and self.sunlight >= 4:
            return "🙂 Okay"
        else:
            return "🥀 Wilting"

    def status(self):
        print(f"\n🌿 Plant: {self.name}")
        print(f"💧 Water Level: {self.water_level}/10")
        print(f"☀️ Sunlight: {self.sunlight}/10")
        print(f"🌱 Growth: {self.growth}/100")
        print(f"🧠 Mood: {self.mood()}\n")

    def water(self):
        if not self.alive:
            print("💧 You can't water a dead plant.")
            return
        self.water_level = min(10, self.water_level + 2)
        print("✅ You watered the plant.")

    def give_sunlight(self):
        if not self.alive:
            print("☀️ Sunlight won't help now.")
            return
        self.sunlight = min(10, self.sunlight + 2)
        print("✅ You gave it sunlight.")

    def pass_time(self):
        if not self.alive:
            return
        self.water_level -= random.randint(1, 2)
        self.sunlight -= random.randint(1, 2)
        if self.water_level <= 0 or self.sunlight <= 0:
            self.alive = False
            print(f"\n😢 {self.name} has died from neglect.")
            return
        self.growth += 5
        print("⏳ Time passed...")

    def is_alive(self):
        return self.alive

# === Run the virtual plant game ===
def run_virtual_plant():
    name = input("🪴 Name your virtual plant: ")
    plant = VirtualPlant(name)

    while plant.is_alive():
        print("\n--- Menu ---")
        print("1. Water the plant")
        print("2. Give sunlight")
        print("3. Check status")
        print("4. Let time pass")
        print("5. Quit")
        choice = input("Choose an action (1-5): ")

        if choice == '1':
            plant.water()
        elif choice == '2':
            plant.give_sunlight()
        elif choice == '3':
            plant.status()
        elif choice == '4':
            plant.pass_time()
        elif choice == '5':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

        time.sleep(1)

# Start the plant simulation
if __name__ == "__main__":
    run_virtual_plant()
