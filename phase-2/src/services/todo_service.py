"""
TodoService for the Console-based In-Memory Todo Application.

This module implements the core business logic for todo operations,
using in-memory storage with a dictionary to map task IDs to Task objects.
"""
from typing import Dict, List, Optional
from models.task import Task


class TodoService:
    """
    Service class for managing tasks in an in-memory todo list.
    
    The service provides operations to add, delete, update, view,
    and mark tasks as complete or incomplete.
    """
    
    def __init__(self):
        """Initialize the TodoService with an empty collection of tasks."""
        self.tasks: Dict[int, Task] = {}
        self.next_id = 1
    
    def add_task(self, title: str) -> Task:
        """
        Creates a new Task with a unique ID and adds it to the collection.
        
        Args:
            title (str): The title of the task
            
        Returns:
            Task: The created task object with a unique ID and incomplete status
            
        Raises:
            ValueError: If the title is empty
        """
        from lib.utils import generate_unique_id
        
        if not title:
            raise ValueError("Task title cannot be empty")
        
        task_id = self.next_id
        self.next_id += 1
        task = Task(id=task_id, title=title, completed=False)
        self.tasks[task_id] = task
        
        return task
    
    def delete_task(self, task_id: int) -> bool:
        """
        Removes a Task from the collection by ID.
        
        Args:
            task_id (str): The ID of the task to delete
            
        Returns:
            bool: True if the task was found and deleted, False otherwise
        """
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False
    
    def update_task(self, task_id: int, new_title: str) -> bool:
        """
        Updates the title of an existing Task.
        
        Args:
            task_id (str): The ID of the task to update
            new_title (str): The new title for the task
            
        Returns:
            bool: True if the task was found and updated, False otherwise
            
        Raises:
            ValueError: If the new title is empty
        """
        if task_id not in self.tasks:
            return False
        
        if not new_title:
            raise ValueError("Task title cannot be empty")
        
        self.tasks[task_id].title = new_title
        return True
    
    def get_all_tasks(self) -> List[Task]:
        """
        Returns all tasks in the collection.
        
        Returns:
            List[Task]: A list of all task objects
        """
        return list(self.tasks.values())
    
    def mark_task_complete(self, task_id: int) -> bool:
        """
        Sets the completion status of a Task to True.
        
        Args:
            task_id (str): The ID of the task to mark complete
            
        Returns:
            bool: True if the task was found and marked complete, False otherwise
        """
        if task_id in self.tasks:
            self.tasks[task_id].completed = True
            return True
        return False
    
    def mark_task_incomplete(self, task_id: int) -> bool:
        """
        Sets the completion status of a Task to False.
        
        Args:
            task_id (str): The ID of the task to mark incomplete
            
        Returns:
            bool: True if the task was found and marked incomplete, False otherwise
        """
        if task_id in self.tasks:
            self.tasks[task_id].completed = False
            return True
        return False
    
    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Gets a task by its ID.
        
        Args:
            task_id (str): The ID of the task to retrieve
            
        Returns:
            Optional[Task]: The task object if found, None otherwise
        """
        return self.tasks.get(task_id)