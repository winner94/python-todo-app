from datetime import datetime

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
        

def main():
    manager = TaskManager()
    manager.add_task("Duolingo")
    manager.add_task("ToDoAPP Python with class")
    manager.add_task("Zrobic kawe")

    manager.list_tasks()
    print("-----")
    manager.complete_task(0)
    manager.list_tasks()
    print("-----")
    manager.remove_task(1)
    manager.list_tasks()

if __name__ == "__main__":
    main()