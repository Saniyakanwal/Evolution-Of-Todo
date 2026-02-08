#!/usr/bin/env python3
"""
CLI Todo Application
A simple command-line interface for managing todos.
"""

import json
from datetime import datetime
from typing import Dict, List, Optional


class Todo:
    """Represents a single todo item."""
    
    def __init__(self, id: int, title: str, description: str = "", status: str = "pending"):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.created_at = datetime.now().isoformat()
    
    def to_dict(self) -> Dict:
        """Convert the Todo object to a dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at
        }


class TodoManager:
    """Manages a collection of Todo items in memory."""
    
    def __init__(self):
        self.todos: List[Todo] = []
        self.next_id = 1
    
    def create_todo(self, title: str, description: str = "") -> Todo:
        """Create a new todo item."""
        todo = Todo(id=self.next_id, title=title, description=description)
        self.todos.append(todo)
        self.next_id += 1
        return todo
    
    def get_todos(self) -> List[Todo]:
        """Get all todos."""
        return self.todos
    
    def get_todo(self, todo_id: int) -> Optional[Todo]:
        """Get a specific todo by ID."""
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None
    
    def update_todo(self, todo_id: int, title: Optional[str] = None, 
                    description: Optional[str] = None, status: Optional[str] = None) -> Optional[Todo]:
        """Update a specific todo."""
        todo = self.get_todo(todo_id)
        if todo:
            if title is not None:
                todo.title = title
            if description is not None:
                todo.description = description
            if status is not None:
                todo.status = status
        return todo
    
    def delete_todo(self, todo_id: int) -> bool:
        """Delete a specific todo."""
        todo = self.get_todo(todo_id)
        if todo:
            self.todos.remove(todo)
            return True
        return False


def print_help():
    """Print help information."""
    print("\nCLI Todo Application")
    print("Commands:")
    print("  add <title> [description]    - Add a new todo")
    print("  list                         - List all todos")
    print("  get <id>                     - Get a specific todo")
    print("  update <id> [title] [desc] [status] - Update a todo")
    print("  complete <id>                - Mark a todo as completed")
    print("  delete <id>                  - Delete a todo")
    print("  quit                         - Exit the application")
    print()


def main():
    """Main function for the CLI Todo application."""
    manager = TodoManager()
    
    print("Welcome to the CLI Todo Application!")
    print_help()
    
    while True:
        try:
            command_input = input("> ").strip().split()
            if not command_input:
                continue
            
            command = command_input[0].lower()
            
            if command == "quit":
                print("Goodbye!")
                break
            elif command == "help":
                print_help()
            elif command == "add":
                if len(command_input) < 2:
                    print("Usage: add <title> [description]")
                    continue
                
                title = command_input[1]
                description = " ".join(command_input[2:]) if len(command_input) > 2 else ""
                
                todo = manager.create_todo(title, description)
                print(f"Added todo: {todo.id} - {todo.title}")
            elif command == "list":
                todos = manager.get_todos()
                if not todos:
                    print("No todos found.")
                else:
                    for todo in todos:
                        status_symbol = "✓" if todo.status == "completed" else "○"
                        print(f"{status_symbol} [{todo.id}] {todo.title}")
                        if todo.description:
                            print(f"    Description: {todo.description}")
                        print(f"    Created: {todo.created_at}")
                        print()
            elif command == "get":
                if len(command_input) != 2:
                    print("Usage: get <id>")
                    continue
                
                try:
                    todo_id = int(command_input[1])
                    todo = manager.get_todo(todo_id)
                    if todo:
                        status_symbol = "✓" if todo.status == "completed" else "○"
                        print(f"{status_symbol} [{todo.id}] {todo.title}")
                        print(f"    Description: {todo.description}")
                        print(f"    Status: {todo.status}")
                        print(f"    Created: {todo.created_at}")
                    else:
                        print(f"Todo with ID {todo_id} not found.")
                except ValueError:
                    print("Invalid ID. Please enter a number.")
            elif command == "update":
                if len(command_input) < 2:
                    print("Usage: update <id> [title] [description] [status]")
                    continue
                
                try:
                    todo_id = int(command_input[1])
                    
                    # Extract optional parameters
                    title = None
                    description = None
                    status = None
                    
                    if len(command_input) >= 3:
                        title = command_input[2]
                    if len(command_input) >= 4:
                        description = command_input[3]
                    if len(command_input) >= 5:
                        status = command_input[4]
                    
                    updated_todo = manager.update_todo(todo_id, title, description, status)
                    if updated_todo:
                        print(f"Updated todo: {updated_todo.id} - {updated_todo.title}")
                    else:
                        print(f"Todo with ID {todo_id} not found.")
                except ValueError:
                    print("Invalid ID. Please enter a number.")
            elif command == "complete":
                if len(command_input) != 2:
                    print("Usage: complete <id>")
                    continue
                
                try:
                    todo_id = int(command_input[1])
                    updated_todo = manager.update_todo(todo_id, status="completed")
                    if updated_todo:
                        print(f"Marked todo as completed: {updated_todo.id} - {updated_todo.title}")
                    else:
                        print(f"Todo with ID {todo_id} not found.")
                except ValueError:
                    print("Invalid ID. Please enter a number.")
            elif command == "delete":
                if len(command_input) != 2:
                    print("Usage: delete <id>")
                    continue
                
                try:
                    todo_id = int(command_input[1])
                    if manager.delete_todo(todo_id):
                        print(f"Deleted todo with ID {todo_id}.")
                    else:
                        print(f"Todo with ID {todo_id} not found.")
                except ValueError:
                    print("Invalid ID. Please enter a number.")
            else:
                print(f"Unknown command: {command}")
                print_help()
        
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()