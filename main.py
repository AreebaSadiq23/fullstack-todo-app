import sys
import questionary
from services import TodoService
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

class InteractiveConsoleApp:
    """
    An interactive console application for the To-Do list manager.
    Uses rich for beautiful output and questionary for interactive prompts.
    """
    def __init__(self):
        self.todo_service = TodoService()
        self.console = Console()

    def _display_menu(self):
        """Displays the main menu and gets user choice via an interactive list."""
        return questionary.select(
            "--- To-Do List Application ---",
            choices=[
                "Create New To-Do Item",
                "View All To-Do Items",
                "View To-Do Item Details by ID",
                "Update To-Do Item",
                "Delete To-Do Item",
                "Exit"
            ]
        ).ask()

    def _get_user_input(self, prompt: str, default: str = "") -> str:
        """Gets string input from the user using questionary."""
        return questionary.text(prompt, default=default).ask().strip()

    def _create_item(self):
        """Handles the creation of a new To-Do item."""
        self.console.print("\n--- Create New To-Do Item ---", style="bold green")
        name = self._get_user_input("Enter item name: ")
        description = self._get_user_input("Enter item description: ")
        
        try:
            new_item = self.todo_service.create_item(name, description)
            self.console.print(f"To-Do Item created successfully! ID: {new_item.id}", style="bold green")
        except ValueError as e:
            self.console.print(f"Error: {e}", style="bold red")

    def _view_all_items(self):
        """Displays all To-Do items in a table."""
        self.console.print("\n--- All To-Do Items ---", style="bold blue")
        items = self.todo_service.get_all_items()
        if not items:
            self.console.print("No To-Do items found.", style="yellow")
            return

        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("ID", style="dim", width=6)
        table.add_column("Name")
        table.add_column("Status")

        for item in items:
            table.add_row(str(item.id), item.name, item.status)
        
        self.console.print(table)

    def _view_item_details(self):
        """Displays detailed information for a specific To-Do item by ID."""
        self.console.print("\n--- View To-Do Item Details ---", style="bold blue")
        item_id = self._get_user_input("Enter the ID of the item to view: ")
        item = self.todo_service.get_item_details(item_id)

        if item:
            self.console.print(Panel(str(item), title=f"Details for ID {item.id}", border_style="blue"))
        else:
            self.console.print(f"Error: To-Do item with ID '{item_id}' not found.", style="bold red")

    def _update_item(self):
        """Handles the update of an existing To-Do item."""
        self.console.print("\n--- Update To-Do Item ---", style="bold yellow")
        item_id = self._get_user_input("Enter the ID of the item to update: ")
        item = self.todo_service.get_item_details(item_id)

        if not item:
            self.console.print(f"Error: To-Do item with ID '{item_id}' not found.", style="bold red")
            return

        self.console.print(Panel(str(item), title=f"Current details for ID {item_id}", border_style="yellow"))

        self.console.print("\nEnter new values (leave blank to keep current value):", style="italic")
        new_name = self._get_user_input(f"New name ({item.name}): ", default=item.name)
        new_description = self._get_user_input(f"New description ({item.description}): ", default=item.description)
        new_status = questionary.select(
            f"New status ({item.status}): ",
            choices=["Pending", "In Progress", "Completed", "Cancelled"],
            default=item.status
        ).ask()

        try:
            updated = self.todo_service.update_item(
                item_id,
                name=new_name if new_name != item.name else None,
                description=new_description if new_description != item.description else None,
                status=new_status if new_status != item.status else None
            )
            if updated:
                self.console.print(f"To-Do item '{item_id}' updated successfully.", style="bold green")
            else:
                self.console.print(f"No changes applied to item '{item_id}'.", style="yellow")
        except ValueError as e:
            self.console.print(f"Error: {e}", style="bold red")

    def _delete_item(self):
        """Handles the deletion of a To-Do item."""
        self.console.print("\n--- Delete To-Do Item ---", style="bold red")
        item_id = self._get_user_input("Enter the ID of the item to delete: ")
        
        if self.todo_service.get_item_details(item_id):
            if questionary.confirm(f"Are you sure you want to delete item '{item_id}'?").ask():
                if self.todo_service.delete_item(item_id):
                    self.console.print(f"To-Do item '{item_id}' deleted successfully.", style="bold green")
                else:
                    self.console.print(f"Error: Could not delete item '{item_id}'.", style="bold red")
        else:
            self.console.print(f"Error: To-Do item with ID '{item_id}' not found.", style="bold red")

    def run(self):
        """Runs the main application loop."""
        while True:
            choice = self._display_menu()

            if choice == "Create New To-Do Item":
                self._create_item()
            elif choice == "View All To-Do Items":
                self._view_all_items()
            elif choice == "View To-Do Item Details by ID":
                self._view_item_details()
            elif choice == "Update To-Do Item":
                self._update_item()
            elif choice == "Delete To-Do Item":
                self._delete_item()
            elif choice == "Exit":
                self.console.print("Exiting To-Do List Application. Goodbye!", style="bold")
                sys.exit(0)
            else:
                self.console.print("Invalid choice. Please select from the menu.", style="bold red")

if __name__ == "__main__":
    app = InteractiveConsoleApp()
    app.run()
