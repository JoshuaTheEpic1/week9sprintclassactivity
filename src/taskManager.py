class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, due_date):
        self.tasks.append(Task(title, description, due_date))

    def find_task_by_title(self, title):
        for task in self.tasks:
            if task.title == title:
                return task
        return None

    def edit_task(self, title, new_title, description, due_date):
        task = self.find_task_by_title(title)
        if task:
            task.title = new_title
            task.description = description
            task.due_date = due_date
        else:
            print("Task not found.")

    def delete_task(self, title):
        task = self.find_task_by_title(title)
        if task:
            self.tasks.remove(task)
        else:
            print("Task not found.")

    def mark_task_as_completed(self, title):
        task = self.find_task_by_title(title)
        if task:
            task.is_completed = True
        else:
            print("Task not found.")

    def print_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"Task {i + 1}:")
            task.print_task()
            print()
