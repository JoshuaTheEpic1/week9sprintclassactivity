#include <iostream>
#include "TaskManager.h"
#include "Task.h"

def main():
    task_manager = TaskManager()
  while True:
    choice = input("Choose an Item: \n 1. Add Item \n 2. Delete Item \n 3. Edit Item \n 4. Filter Items \n 5. Mark Item as complete \n")
    match choice:
    case '1': 
      print("add")
    case '2': 
      print("delete")
    case '3': 
      print("Edit")
    case '4': 
      print("filter")
    case '5': 
      print("complete")
    case _:
      print("invalid option")


if __name__ == "__main__":
    main()
