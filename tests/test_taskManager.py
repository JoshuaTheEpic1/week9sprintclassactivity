import pytest
import taskManager

@pytest.fixture
def task_manager():
    manager = TaskManager()
    manager.tasks = [
        Task("Task A", "2024-11-19", False),
        Task("Task B", "2024-11-20", True),
        Task("Task C", "2024-11-21", False),
    ]
    return manager

def test_sort_tasks_by_title(task_manager):
    task_manager.sort_tasks(by="title")
    assert [task.title for task in task_manager.tasks] == ["Task A", "Task B", "Task C"]

    task_manager.sort_tasks(by="title", reverse=True)
    assert [task.title for task in task_manager.tasks] == ["Task C", "Task B", "Task A"]

def test_sort_tasks_by_due_date(task_manager):
    task_manager.sort_tasks(by="due_date")
    assert [task.due_date for task in task_manager.tasks] == ["2024-11-19", "2024-11-20", "2024-11-21"]

def test_sort_tasks_by_completed(task_manager):
    task_manager.sort_tasks(by="completed")
    assert [task.is_completed for task in task_manager.tasks] == [False, False, True]

def test_filter_tasks_by_title(task_manager):
    filtered = task_manager.filter_tasks(title_contains="A")
    assert len(filtered) == 1
    assert filtered[0].title == "Task A"

def test_filter_tasks_by_due_date(task_manager):
    filtered = task_manager.filter_tasks(due_date="2024-11-20")
    assert len(filtered) == 1
    assert filtered[0].due_date == "2024-11-20"

def test_filter_tasks_by_completed(task_manager):
    filtered = task_manager.filter_tasks(completed=True)
    assert len(filtered) == 1
    assert filtered[0].is_completed is True
from src import taskManager



def test_add_task():
    manager = taskManager.TaskManager()
    manager.add_task('Alpha', 'Beta', 'Now')
    manager.add_task('Gamma', 'Omega', 'Then')
    assert len(manager.tasks) == 2
    manager.add_task('Theta', 'Phi', 'Later')
    assert len(manager.tasks) == 3

def test_find_task_by_title():
    manager = taskManager.TaskManager()
    manager.add_task('Alpha', 'Beta', 'Now')
    manager.add_task('Gamma', 'Omega', 'Then')
    #test exist
    assert manager.find_task_by_title('Gamma').description == 'Omega'
    #test not exist
    assert manager.find_task_by_title('Zeta') is None