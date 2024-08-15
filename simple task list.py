import json
from typing import List, Dict, Optional

# Define a Task class
class Task:
    def _init_(self, description: str, priority: int):
        self.description = description
        self.priority = priority

    def _repr_(self):
        return f"Task(description='{self.description}', priority={self.priority})"

# Define a TaskManager class
class TaskManager:
    def _init_(self):
        self.tasks: List[Task] = []

    def add_task(self, description: str, priority: int):
        new_task = Task(description, priority)
        self.tasks.append(new_task)
        print(f"Task added: {new_task}")

    def remove_task(self, description: str):
        self.tasks = [task for task in self.tasks if task.description != description]
        print(f"Removed tasks with description: {description}")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for task in sorted(self.tasks, key=lambda t: t.priority, reverse=True):
            print(f"Description: {task.description}, Priority: {task.priority}")

    def prioritize_tasks(self):
        self.tasks = sorted(self.tasks, key=lambda t: t.priority, reverse=True)
        print("Tasks prioritized.")

    def recommend_tasks(self, keyword: str) -> List[Task]:
        recommended = [task for task in self.tasks if keyword.lower() in task.description.lower()]
        return recommended

    def save_tasks(self, filename: str):
        with open(filename, 'w') as file:
            json.dump([task._dict_ for task in self.tasks], file)
        print(f"Tasks saved to {filename}")

    def load_tasks(self, filename: str):
        try:
            with open(filename, 'r') as file:
                tasks_data = json.load(file)
                self.tasks = [Task(**task) for task in tasks_data]
            print(f"Tasks loaded from {filename}")
        except FileNotFoundError:
            print("File not found.")

# Define a function for the main application interface
def main():
    task_manager = TaskManager()
    
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Prioritize Tasks")
        print("5. Recommend Tasks")
        print("6. Save Tasks")
        print("7. Load Tasks")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            priority = int(input("Enter task priority (1-10): "))
            task_manager.add_task(description, priority)

        elif choice == '2':
            description = input("Enter task description to remove: ")
            task_manager.remove_task(description)

        elif choice == '3':
            task_manager.list_tasks()

        elif choice == '4':
            task_manager.prioritize_tasks()

        elif choice == '5':
            keyword = input("Enter keyword for task recommendation: ")
            recommendations = task_manager.recommend_tasks(keyword)
            if recommendations:
                print("Recommended tasks:")
                for task in recommendations:
                    print(task)
            else:
                print("No tasks found with that keyword.")

        elif choice == '6':
            filename = input("Enter filename to save tasks: ")
            task_manager.save_tasks(filename)

        elif choice == '7':
            filename = input("Enter filename to load tasks: ")
            task_manager.load_tasks(filename)

        elif choice == '8':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if _name_ == "_main_":
    main()