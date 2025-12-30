# Development Tasks for CLI Todo Application

1.  **Project Scaffolding: Directories**
    - Create the `src/` directory for all Python source code.

2.  **Project Scaffolding: Initial Files**
    - Create an empty file `src/__init__.py`.
    - Create an empty file `src/models.py`.
    - Create an empty file `src/storage.py`.
    - Create an empty file `src/services.py`.
    - Create an empty file `src/main.py`.

3.  **Project Documentation: README**
    - Create the `README.md` file with a basic project title and description.

4.  **Project Documentation: AI Guidelines**
    - Create the `CLAUDE.md` file with placeholder content describing AI development rules.

5.  **Data Model: Task Class**
    - In `src/models.py`, define the `Task` dataclass with fields: `id: int`, `title: str`, `description: str`, `status: str`.

6.  **Storage Layer: Initialization**
    - In `src/storage.py`, create a module-level `_tasks` list to store task objects and a `_next_id` integer counter initialized to 1.

7.  **Storage Layer: Add Task Function**
    - In `src/storage.py`, implement the `add_task(title: str, description: str)` function that creates a `Task`, assigns a new ID, adds it to the `_tasks` list, and returns the new task.

8.  **Storage Layer: Get Task Functions**
    - In `src/storage.py`, implement `get_all_tasks()` to return all tasks.
    - In `src/storage.py`, implement `get_task_by_id(task_id: int)` to find and return a single task or `None`.

9.  **Storage Layer: Delete Task Function**
    - In `src/storage.py`, implement `delete_task(task_id: int)` that removes a task from the `_tasks` list and returns `True` on success or `False` if the task was not found.

10. **Storage Layer: Update Task Function**
    - In `src/storage.py`, implement `update_task(task: Task)` that replaces the existing task with the same ID in the `_tasks` list.

11. **Service Layer: Custom Exception**
    - In `src/services.py`, define a custom exception `class TaskNotFoundError(Exception): pass`.

12. **Service Layer: Add and Get Services**
    - In `src/services.py`, implement `add_task(title: str, description: str)` which calls the corresponding storage function.
    - In `src/services.py`, implement `get_all_tasks()` which calls the corresponding storage function.

13. **Service Layer: Delete Service**
    - In `src/services.py`, implement `delete_task(task_id: int)`. It should call `storage.delete_task` and raise `TaskNotFoundError` if the deletion fails.

14. **Service Layer: Update Service**
    - In `src/services.py`, implement `update_task(task_id: int, title: str | None, description: str | None)`. It must fetch the task, update its fields if new values are provided, and then save it back to storage. It must raise `TaskNotFoundError` if the task doesn't exist.

15. **Service Layer: Status Update Service**
    - In `src/services.py`, implement `update_task_status(task_id: int, status: str)`. It must fetch the task, update its status, and save it. It must raise `TaskNotFoundError` if the task doesn't exist.

16. **CLI: Argparse Setup**
    - In `src/main.py`, set up `argparse` to create a main command-line parser with subparsers for `add`, `list`, `update`, `delete`, `complete`, and `incomplete`.

17. **CLI: `list` Command**
    - In `src/main.py`, implement the logic for the `list` command to call `services.get_all_tasks()` and print the formatted results to the console.

18. **CLI: `add` Command**
    - In `src/main.py`, add arguments `--title` (required) and `--description` (optional) to the `add` subparser. Implement the handler to call `services.add_task` and print a success message.

19. **CLI: `delete` Command**
    - In `src/main.py`, add a positional `task_id` argument to the `delete` subparser. Implement the handler to call `services.delete_task`.

20. **CLI: `update` Command**
    - In `src/main.py`, add a positional `task_id` argument and optional `--title` and `--description` arguments to the `update` subparser. Implement the handler to call `services.update_task`.

21. **CLI: `complete` and `incomplete` Commands**
    - In `src/main.py`, add a positional `task_id` argument to the `complete` and `incomplete` subparsers. Implement handlers to call `services.update_task_status` with "complete" or "incomplete" respectively.

22. **CLI: Error Handling**
    - In `src/main.py`, wrap the service calls for each command handler in a `try...except TaskNotFoundError` block to print user-friendly error messages to `sys.stderr`.