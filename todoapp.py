from datetime import datetime

class Task:
    def __init__(self, title):
        self.title = title
        self.done = False
        self.created_at = datetime.now().strftime("%Y-%m-%d")

    def __str__(self):
        status = "✓" if self.done else "x"
        return f"[{status}] {self.title} {self.created_at}"

def main():
    task1 = Task("Duolingo")
    task2 = Task("ToDoApp with class")

    print(task1.title)
    print(task1.done)
    print(task1.created_at)
    print("----------------")
    print(task1)

if __name__ == "__main__":
    main()