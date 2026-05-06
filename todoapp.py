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
    manager.add_task("Duolingo")
    manager.add_task("ToDoApp")
    manager.complete_task(0)
    manager.save()
    
    manager2 = TaskManager()
    manager2.load()
    manager2.list_tasks()

if __name__ == "__main__":
    main()