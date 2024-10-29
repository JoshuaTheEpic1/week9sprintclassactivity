from taskManager import TaskManager
from task import Task

def main():
    task_manager = TaskManager()
  while True:
    choice = input("Choose an Item: \n 1. Add Item \n 2. Delete Item \n 3. Edit Item \n 4. Filter Items \n 5. Mark Item as complete \n")
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
      task_manager.filter_tasks()
    case '5': 
      task = input("enter title of task to mark complete \n")
      task_manager.mark_task_as_completed(task)
    case _:
      print("invalid option")


if __name__ == "__main__":
    main()
