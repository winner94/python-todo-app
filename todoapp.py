from datetime import datetime
import json

class Task:
    def __init__(self, title):
        self.title = title
        self.done = False
        self.created_at = datetime.now().strftime("%Y-%m-%d")

    def __str__(self):
        status = "✓" if self.done else "x"
        return f"[{status}] {self.title} {self.created_at}"

class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)

    def complete_task(self, index):
        self.tasks[index].done = True
    
    def remove_task(self,index):
        self.tasks.pop(index)

    def list_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}")

    def save(self):
        tasks_list = [{"title": task.title, "done": task.done, "created_at": task.created_at} for task in self.tasks]

        with open("tasks.json", "w") as f:
            json.dump(tasks_list, f) 

    def load(self):
        try:
            with open("tasks.json", "r") as f:
                tasks_lists = json.load(f)
        except FileNotFoundError:
            return "File \"tasks.json\" not found."
        
        for task_data in tasks_lists:
            task = Task(task_data["title"])
            task.done = task_data["done"]
            task.created_at = task_data["created_at"]
            self.tasks.append(task)
            

def main():
    manager = TaskManager()
    manager.load()
    print("***** TODO APP *****")
    while True:
        print("--- MENU ---")
        print("1. Add task")
        print("2. Complete task")
        print("3. Remove task")
        print("4. List tasks")
        print("5. Quit")

        choice = int(input("Choose action [1-5]: "))
        if choice == 5:
            break

        if choice == 1:
            t_name = input("Task name: ")
            manager.add_task(t_name)
            manager.save()
        
        if choice == 2:
            t_done = int(input("Task number to mark as done: "))
            manager.complete_task(t_done)
            manager.save()
            
        if choice == 3:
            manager.list_tasks()
            t_remove = int(input("Task to remove: "))
            manager.remove_task(t_remove)
            manager.save()

        if choice == 4:
            manager.list_tasks()

if __name__ == "__main__":
    main()