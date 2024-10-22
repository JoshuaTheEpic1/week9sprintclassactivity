class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, due_date):
        self.tasks.append(Task(title, description, due_date))

    def edit_task(self, index, title, description, due_date):
        if 0 <= index < len(self.tasks):
            self.tasks[index].title = title
            self.tasks[index].description = description
            self.tasks[index].due_date = due_date
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            print("Invalid task index.")

    def mark_task_as_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].is_completed = True
        else:
            print("Invalid task index.")

    def print_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"Task {i + 1}:")
            task.print_task()
            print()
