from typing import List, Optional
from models import TodoItem
from storage import InMemoryStorage

class TodoService:
    """
    Provides business logic for managing TodoItem objects.
    Interacts with InMemoryStorage for data operations.
    """
    def __init__(self):
        self._storage = InMemoryStorage()

    def create_item(self, name: str, description: str, status: str = "Pending") -> TodoItem:
        """
        Creates a new To-Do item and adds it to storage.

        Args:
            name (str): The name of the To-Do item.
            description (str): The description of the To-Do item.
            status (str): The initial status of the To-Do item.

        Returns:
            TodoItem: The newly created To-Do item.
        """
        if not name or not description:
            raise ValueError("Name and description cannot be empty.")
        item = TodoItem(name, description, status)
        self._storage.add_item(item)
        return item

    def get_all_items(self) -> List[TodoItem]:
        """
        Retrieves all To-Do items.

        Returns:
            List[TodoItem]: A list of all To-Do items.
        """
        return self._storage.get_all_items()

    def get_item_details(self, item_id: str) -> Optional[TodoItem]:
        """
        Retrieves details of a specific To-Do item by its ID.

        Args:
            item_id (str): The ID of the To-Do item to retrieve.

        Returns:
            Optional[TodoItem]: The To-Do item if found, None otherwise.
        """
        return self._storage.get_item_by_id(item_id)

    def update_item(self, item_id: str, name: Optional[str] = None,
                    description: Optional[str] = None, status: Optional[str] = None) -> bool:
        """
        Updates an existing To-Do item.

        Args:
            item_id (str): The ID of the item to update.
            name (Optional[str]): New name for the item.
            description (Optional[str]): New description for the item.
            status (Optional[str]): New status for the item.

        Returns:
            bool: True if the item was updated, False otherwise (e.g., item not found).
        """
        item_data = {}
        if name is not None:
            if not name.strip():
                raise ValueError("Name cannot be empty.")
            item_data["name"] = name
        if description is not None:
            if not description.strip():
                raise ValueError("Description cannot be empty.")
            item_data["description"] = description
        if status is not None:
            if status not in ["Pending", "Completed", "In Progress", "Cancelled"]:
                raise ValueError("Invalid status. Allowed: Pending, Completed, In Progress, Cancelled.")
            item_data["status"] = status

        if not item_data:
            print("No fields provided for update.")
            return False

        return self._storage.update_item(item_id, item_data)

    def delete_item(self, item_id: str) -> bool:
        """
        Deletes a To-Do item by its ID.

        Args:
            item_id (str): The ID of the item to delete.

        Returns:
            bool: True if the item was deleted, False otherwise (e.g., item not found).
        """
        return self._storage.delete_item(item_id)
