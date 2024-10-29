from task import task

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, due_date):
        self.tasks.append(task(title, description, due_date))

    def find_task_by_title(self, title) -> task:
        for task in self.tasks:
            if task.title == title:
                return task
        return None

    def edit_task(self, title, new_title = None, description = None, due_date = None):
        task = self.find_task_by_title(title)
        if task:
            task.title = new_title if new_title != None else task.title
            task.description = description if description != None else task.description
            task.dueDate = due_date if due_date != None else task.dueDate
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

    def sort_tasks(self, by="title", reverse=False):
        if by == "title":
            self.tasks.sort(key=lambda task: task.title, reverse=reverse)
        elif by == "due_date":
            self.tasks.sort(key=lambda task: task.due_date, reverse=reverse)
        elif by == "completed":
            self.tasks.sort(key=lambda task: task.is_completed, reverse=reverse)
        else:
            print("Invalid sort key. Use 'title', 'due_date', or 'completed'.")

    def filter_tasks(self, title_contains=None, due_date=None, completed=None):
        filtered_tasks = self.tasks
        if title_contains:
            filtered_tasks = [task for task in filtered_tasks if title_contains.lower() in task.title.lower()]
        if due_date:
            filtered_tasks = [task for task in filtered_tasks if task.due_date == due_date]
        if completed is not None:
            filtered_tasks = [task for task in filtered_tasks if task.is_completed == completed]
        
        for i, task in enumerate(filtered_tasks):
            print(f"Task {i + 1}:")
            task.print_task()
            print()

    def print_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"Task {i + 1}:")
            task.print_task()
            print()
