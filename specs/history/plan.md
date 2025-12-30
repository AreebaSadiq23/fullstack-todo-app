# Implementation Plan for CLI Todo Application

## 1. Overall Architecture

The application will follow a clean, layered architecture to separate concerns. This promotes maintainability and testability, adhering to the principles outlined in the constitution. The project will be structured under a `src/` directory.

The core components are:
- **`main.py` (Presentation Layer):** The entry point for the CLI. Responsible for parsing commands and arguments, interacting with the service layer, and displaying output to the user.
- **`services.py` (Business Logic Layer):** Contains the core application logic. It orchestrates operations like creating, updating, and deleting tasks. It is completely decoupled from the CLI interface.
- **`storage.py` (Data Access Layer):** Manages the in-memory data store. It directly manipulates the list of tasks and handles ID generation.
- **`models.py` (Data Model):** Defines the data structures used throughout the application, primarily the `Task` model.

## 2. Module Responsibilities

### `src/models.py`
- Defines a `Task` data class using `dataclasses.dataclass`.
- The `Task` class will contain the following fields:
    - `id`: `int` (Unique identifier)
    - `title`: `str`
    - `description`: `str`
    - `status`: `str` (Enum or string, e.g., "incomplete", "complete")

### `src/storage.py`
- Contains a private, module-level list `_tasks` to store the `Task` objects.
- Contains a private, module-level counter `_next_id` for generating unique task IDs.
- Exposes functions to interact with the `_tasks` list:
    - `get_all_tasks()`: Returns a copy of the entire task list.
    - `get_task_by_id(task_id: int)`: Returns a specific task or `None` if not found.
    - `add_task(title: str, description: str)`: Creates a new `Task`, assigns an ID, adds it to the list, and returns the newly created task.
    - `update_task(task_id: int, title: str, description: str)`: Finds a task by ID and updates its fields.
    - `delete_task(task_id: int)`: Removes a task from the list by its ID.
    - `_generate_id()`: Internal helper to increment and return the next available ID.

### `src/services.py`
- Acts as a bridge between the CLI and the data storage.
- Imports functions from `storage.py`.
- Defines functions that map to user actions:
    - `add_task(title: str, description: str)`: Calls the storage layer to add a task.
    - `get_all_tasks()`: Retrieves all tasks.
    - `update_task(task_id: int, title: str | None, description: str | None)`: Retrieves the existing task, updates its attributes with the provided values, and calls the storage layer to save the changes.
    - `delete_task(task_id: int)`: Calls the storage layer to delete a task.
    - `update_task_status(task_id: int, status: str)`: Updates the status of a specific task.
- This layer will be responsible for raising business-logic-specific exceptions, such as `TaskNotFoundError`.

### `src/main.py`
- Uses the `argparse` standard library module to define and parse CLI commands.
- Will define a main parser and subparsers for each command.
- Catches exceptions from the service layer to provide user-friendly error messages.
- Formats and prints task data to the console for the `view` command.
- Prints clear success or error messages for all operations.

## 3. CLI Command Flow

The application will be invoked via a main script. The command structure will be as follows, using subparsers for actions.

- **Add a task:**
  ```bash
  python src/main.py add --title "My new task" --description "A detailed description."
  ```
- **View all tasks:**
  ```bash
  python src/main.py list
  ```
- **Update a task:**
  ```bash
  python src/main.py update 1 --title "Updated title" --description "Updated description."
  ```
  *(Note: Updating title or description will be optional)*
- **Delete a task:**
  ```bash
  python src/main.py delete 1
  ```
- **Mark a task complete:**
  ```bash
  python src/main.py complete 1
  ```
- **Mark a task incomplete:**
  ```bash
  python src/main.py incomplete 1
  ```

## 4. Task Data Model

The primary data model will be the `Task` class defined in `src/models.py`.

```python
from dataclasses import dataclass

@dataclass
class Task:
    id: int
    title: str
    description: str
    status: str # "complete" or "incomplete"
```

## 5. Error Handling Strategy

- **Business Logic Errors:** The `services` layer will define and raise custom exceptions for predictable error states.
    - `TaskNotFoundError`: Raised when an operation is requested on a task ID that does not exist.
- **CLI/Presentation Layer:** The `main.py` script will contain `try...except` blocks in the handlers for each command.
    - It will catch specific exceptions (like `TaskNotFoundError`) and print a friendly message to `sys.stderr`.
    - A general `except Exception` will catch any unexpected errors and print a generic error message.
- **Input Validation:** The `argparse` library will automatically handle errors related to missing or malformed command-line arguments.
- **Success Messages:** For every successful write operation (add, update, delete, status change), a confirmation message will be printed to `sys.stdout`.
