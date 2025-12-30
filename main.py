import sys
from services import TodoService

class ConsoleApp:
    """
    Main console application for the To-Do list manager.
    Handles user interaction, menu display, and delegates to TodoService.
    """
    def __init__(self):
        self.todo_service = TodoService()

    def _display_menu(self):
        """Displays the main menu options to the user."""
        print("\n--- To-Do List Application ---")
        print("1. Create New To-Do Item")
        print("2. View All To-Do Items")
        print("3. View To-Do Item Details by ID")
        print("4. Update To-Do Item")
        print("5. Delete To-Do Item")
        print("6. Exit")
        print("----------------------------")

    def _get_user_input(self, prompt: str) -> str:
        """Gets string input from the user."""
        return input(prompt).strip()

    def _create_item(self):
        """Handles the creation of a new To-Do item."""
        print("\n--- Create New To-Do Item ---")
        name = self._get_user_input("Enter item name: ")
        description = self._get_user_input("Enter item description: ")
        
        try:
            new_item = self.todo_service.create_item(name, description)
            print(f"To-Do Item created successfully! ID: {new_item.id}")
        except ValueError as e:
            print(f"Error: {e}")

    def _view_all_items(self):
        """Displays all To-Do items."""
        print("\n--- All To-Do Items ---")
        items = self.todo_service.get_all_items()
        if not items:
            print("No To-Do items found.")
            return

        for item in items:
            print(f"ID: {item.id}, Name: {item.name}, Status: {item.status}")
        print("-----------------------")

    def _view_item_details(self):
        """Displays detailed information for a specific To-Do item by ID."""
        print("\n--- View To-Do Item Details ---")
        item_id = self._get_user_input("Enter the ID of the item to view: ")
        item = self.todo_service.get_item_details(item_id)

        if item:
            print(item)
        else:
            print(f"Error: To-Do item with ID '{item_id}' not found.")
        print("-----------------------------")

    def _update_item(self):
        """Handles the update of an existing To-Do item."""
        print("\n--- Update To-Do Item ---")
        item_id = self._get_user_input("Enter the ID of the item to update: ")
        item = self.todo_service.get_item_details(item_id)

        if not item:
            print(f"Error: To-Do item with ID '{item_id}' not found.")
            return

        print(f"Current details for ID '{item_id}':")
        print(item)

        print("\nEnter new values (leave blank to keep current value):")
        new_name = self._get_user_input(f"New name ({item.name}): ")
        new_description = self._get_user_input(f"New description ({item.description}): ")
        new_status = self._get_user_input(f"New status ({item.status}) [Pending, Completed, In Progress, Cancelled]: ")

        try:
            updated = self.todo_service.update_item(
                item_id,
                name=new_name if new_name else None,
                description=new_description if new_description else None,
                status=new_status if new_status else None
            )
            if updated:
                print(f"To-Do item '{item_id}' updated successfully.")
            else:
                print(f"No changes applied to item '{item_id}'.")
        except ValueError as e:
            print(f"Error: {e}")
        print("-------------------------")


    def _delete_item(self):
        """Handles the deletion of a To-Do item."""
        print("\n--- Delete To-Do Item ---")
        item_id = self._get_user_input("Enter the ID of the item to delete: ")
        
        if self.todo_service.delete_item(item_id):
            print(f"To-Do item '{item_id}' deleted successfully.")
        else:
            print(f"Error: To-Do item with ID '{item_id}' not found.")
        print("-------------------------")


    def run(self):
        """Runs the main application loop."""
        while True:
            self._display_menu()
            choice = self._get_user_input("Enter your choice: ")

            if choice == '1':
                self._create_item()
            elif choice == '2':
                self._view_all_items()
            elif choice == '3':
                self._view_item_details()
            elif choice == '4':
                self._update_item()
            elif choice == '5':
                self._delete_item()
            elif choice == '6':
                print("Exiting To-Do List Application. Goodbye!")
                sys.exit(0)
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    app = ConsoleApp()
    app.run()
