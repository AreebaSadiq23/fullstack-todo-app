from typing import List, Optional, Dict
from models import TodoItem

class InMemoryStorage:
    """
    Manages in-memory storage for TodoItem objects.
    Provides CRUD operations without any persistence.
    """
    def __init__(self):
        self._items: List[TodoItem] = []

    def add_item(self, item: TodoItem) -> None:
        """Adds a new TodoItem to storage."""
        self._items.append(item)

    def get_all_items(self) -> List[TodoItem]:
        """Retrieves all TodoItem objects from storage."""
        return list(self._items)  # Return a copy to prevent external modification

    def get_item_by_id(self, item_id: str) -> Optional[TodoItem]:
        """Retrieves a single TodoItem by its ID."""
        for item in self._items:
            if item.id == item_id:
                return item
        return None

    def update_item(self, item_id: str, new_data: Dict[str, str]) -> bool:
        """
        Updates an existing TodoItem by its ID with new data.

        Args:
            item_id (str): The ID of the item to update.
            new_data (Dict[str, str]): A dictionary containing fields to update.

        Returns:
            bool: True if the item was found and updated, False otherwise.
        """
        item = self.get_item_by_id(item_id)
        if item:
            for key, value in new_data.items():
                if hasattr(item, key):
                    setattr(item, key, value)
            return True
        return False

    def delete_item(self, item_id: str) -> bool:
        """
        Deletes a TodoItem from storage by its ID.

        Args:
            item_id (str): The ID of the item to delete.

        Returns:
            bool: True if the item was found and deleted, False otherwise.
        """
        initial_count = len(self._items)
        self._items = [item for item in self._items if item.id != item_id]
        return len(self._items) < initial_count
