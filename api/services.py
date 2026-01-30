from typing import List, Optional
from models import Task
from storage import (
    get_all_tasks as storage_get_all_tasks,
    get_task_by_id as storage_get_task_by_id,
    add_task as storage_add_task,
    update_task as storage_update_task,
    delete_task as storage_delete_task,
    update_task_status as storage_update_task_status,
)

def get_all_tasks() -> List[Task]:
    """
    Get all tasks.
    """
    return storage_get_all_tasks()

def get_task_by_id(task_id: int) -> Optional[Task]:
    """
    Get a single task by ID.
    """
    return storage_get_task_by_id(task_id)

def add_task(title: str, description: str) -> Task:
    """
    Create a new task.
    """
    if not title or not description:
        raise ValueError("Title and description cannot be empty.")
    return storage_add_task(title, description)

def update_task(task_id: int, title: str | None, description: str | None) -> Optional[Task]:
    """
    Update a task.
    """
    return storage_update_task(task_id, title, description)

def delete_task(task_id: int) -> None:
    """
    Delete a task.
    """
    storage_delete_task(task_id)

def update_task_status(task_id: int, status: str) -> Optional[Task]:
    """
    Update the status of a task.
    """
    return storage_update_task_status(task_id, status)