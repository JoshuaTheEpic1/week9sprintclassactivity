class Task:
    def __init__(self, description:str, title:str, dueDate:str) -> None:
        self.description = description
        self.title = title
        self.due_date = dueDate
        self.is_completed = False

    def __str__(self) -> str:
        return f"Title: {self.title} Description: {self.description} Due Date: {self.due_date} Completed: {'Yes' if self.is_completed else 'No'}"
