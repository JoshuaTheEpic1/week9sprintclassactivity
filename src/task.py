class task:
    def __init__(self, description:str, title:str, dueDate:str) -> None:
        self.description = description
        self.title = title
        self.dueDate = dueDate
        self.is_completed = False

    def __str__(self) -> str:
        return f"Title: {self.title} Description: {self.description} Due Date: {self.dueDate} Completed: {'Yes' if self.is_completed else 'No'}"
