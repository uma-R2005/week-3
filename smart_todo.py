from datetime import datetime

class Task:
    def __init__(self, title, due_date, priority='medium'):
        self.title = title
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.priority = priority.lower()
        self.completed = False

    def days_left(self):
        return (self.due_date - datetime.now()).days

    def status_emoji(self):
        if self.completed:
            return "✅"
        elif self.days_left() < 0:
            return "⚠️"
        elif self.priority == 'high':
            return "🔥"
        elif self.priority == 'low':
            return "🧊"
        else:
            return "📝"

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        return f"{self.status_emoji()} {self.title} (Due: {self.due_date.date()}, Priority: {self.priority.capitalize()}, Completed: {'Yes' if self.completed else 'No'})"

class SmartToDoList:
    def __init__(self):
        self.tasks = []

        # ✅ Preloaded tasks
        self.tasks.append(Task("Submit science project", "2025-08-27", "high"))
        self.tasks.append(Task("Pay electricity bill", "2025-08-26", "medium"))
        self.tasks.append(Task("Buy birthday gift for friend", "2025-08-30", "low"))

    def add_task(self):
        title = input("Enter task title: ")
        due_date = input("Enter due date (YYYY-MM-DD): ")
        priority = input("Enter priority (high/medium/low): ")
        try:
            task = Task(title, due_date, priority)
            self.tasks.append(task)
            print("✅ Task added successfully!")
        except ValueError:
            print("❌ Invalid date format. Please use YYYY-MM-DD.")

    def show_tasks(self):
        if not self.tasks:
            print("📭 No tasks added yet.")
            return

        print("\n📋 Your Smart To-Do List:")
        for idx, task in enumerate(self.tasks, 1):
            print(f"[{idx}] {task}")

    def complete_task(self):
        self.show_tasks()
        if not self.tasks:
            return
        try:
            index = int(input("Enter the task number to mark complete: "))
            if 0 < index <= len(self.tasks):
                self.tasks[index - 1].mark_complete()
                print("✅ Task marked as complete.")
            else:
                print("❌ Invalid task number.")
        except ValueError:
            print("❌ Please enter a valid number.")

    def run(self):
        while True:
            print("\n📌 Menu:")
            print("1. Add a task")
            print("2. Show tasks")
            print("3. Mark task complete")
            print("4. Exit")
            choice = input("Choose an option (1-4): ")

            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.show_tasks()
            elif choice == '3':
                self.complete_task()
            elif choice == '4':
                print("👋 Goodbye! Stay productive.")
                break
            else:
                print("❌ Invalid choice. Try again.")

# Run the app
if __name__ == "__main__":
    todo = SmartToDoList()
    todo.run()
