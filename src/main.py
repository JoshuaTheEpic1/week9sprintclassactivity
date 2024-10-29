from taskManager import TaskManager
from task import Task

def get_filter_input():
    title_contains = input("Enter a title to filter by (or leave blank): ").strip()
    due_date = input("Enter a due date to filter by (YYYY-MM-DD) (or leave blank): ").strip()
    completed_input = input("Filter by completion status? (yes/no/leave blank): ").strip().lower()

    if completed_input == "yes":
        completed = True
    elif completed_input == "no":
        completed = False
    else:
        completed = None

    reverse_input = input("Sort in reverse order? (yes/no): ").strip().lower()
    reverse = reverse_input == "yes"

    return title_contains, due_date, completed, reverse

def main():
  task_manager = TaskManager()
  while True:
    choice = input("Choose an Item: \n 1. Add Item \n 2. Delete Item \n 3. Edit Item \n 4. Filter Items \n 5. Mark Item as complete \n")
    task_manager.print_tasks()
    match choice:
      case '1': 
        title = input("enter a title: \n")
        description = input("enter a description: \n")
        due_date = input("enter a due date: \n")
        task_manager.add_task(title, description, due_date)
      case '2': 
        dead_task = input("enter title of task to delete \n")
        task_manager.delete_task(dead_task)
      case '3': 
        title = input("enter a title: \n")
        description = input("enter a description: \n")
        due_date = input("enter a due date: \n")
        task_manager.edit_task(title, description, due_date)
      case '4': 
        title_contains, due_date, completed, reverse = get_filter_input()
        task_manager.filter_tasks(title, due_date, completed, reverse)
      case '5': 
        task = input("enter title of task to mark complete \n")
        task_manager.mark_task_as_completed(task)
      case _:
        print("invalid option")


if __name__ == "__main__":
    main()
