import uuid

class TodoItem:
    """
    Represents a single To-Do item.

    Attributes:
        id (str): A unique identifier for the To-Do item. Auto-generated.
        name (str): The name/title of the To-Do item.
        description (str): A detailed description of the To-Do item.
        status (str): The current status of the To-Do item (e.g., "Pending", "Completed").
    """
    def __init__(self, name: str, description: str, status: str = "Pending"):
        self.id = str(uuid.uuid4())[:8]  # Generate a short unique ID
        self.name = name
        self.description = description
        self.status = status

    def __str__(self):
        return (f"ID: {self.id}\n"
                f"  Name: {self.name}\n"
                f"  Description: {self.description}\n"
                f"  Status: {self.status}")

    def to_dict(self):
        """Converts the TodoItem object to a dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "status": self.status
        }
