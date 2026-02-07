"""
Task model for the Console-based In-Memory Todo Application.

This module defines the Task entity with id, title, and completion status attributes.
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    """
    Represents a todo item that has a unique identifier, title text, and completion status.
    
    Attributes:
        id (str): A unique identifier for the task (UUID string)
        title (str): The description/title of the task (non-empty string)
        completed (bool): The completion status of the task (default: False)
    """
    id: str
    title: str
    completed: bool = False
    
    def __post_init__(self):
        """Validate the Task attributes after initialization."""
        if not self.id:
            raise ValueError("Task ID cannot be empty")
        if self.title is None or self.title.strip() == "":
            raise ValueError("Task title cannot be empty")