import pytest
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