from typing import List, Optional
from models import Task

_tasks: List[Task] = []
_next_id = 1

def get_all_tasks() -> List[Task]:
    """
    Get all tasks.
    """
    return _tasks

def get_task_by_id(task_id: int) -> Optional[Task]:
    """
    Get a single task by ID.
    """
    for task in _tasks:
        if task.id == task_id:
            return task
    return None

def add_task(title: str, description: str) -> Task:
    """
    Create a new task.
    """
    global _next_id
    task = Task(id=_next_id, title=title, description=description)
    _tasks.append(task)
    _next_id += 1
    return task

def update_task(task_id: int, title: str | None, description: str | None) -> Optional[Task]:
    """
    Update a task.
    """
    task = get_task_by_id(task_id)
    if task:
        if title:
            task.title = title
        if description:
            task.description = description
    return task

def delete_task(task_id: int) -> None:
    """
    Delete a task.
    """
    global _tasks
    _tasks = [task for task in _tasks if task.id != task_id]

def update_task_status(task_id: int, status: str) -> Optional[Task]:
    """
    Update the status of a task.
    """
    task = get_task_by_id(task_id)
    if task:
        task.status = status
    return task