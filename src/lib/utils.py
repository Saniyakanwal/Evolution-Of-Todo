"""
Utility functions for the Console-based In-Memory Todo Application.
"""
import uuid


def generate_unique_id() -> str:
    """
    Generate a unique identifier string.
    
    Returns:
        str: A unique identifier string (UUID4 format)
    """
    return str(uuid.uuid4())


def validate_task_title(title: str) -> bool:
    """
    Validate that a task title is not empty or None.
    
    Args:
        title (str): The title to validate
        
    Returns:
        bool: True if the title is valid, False otherwise
    """
    return title is not None and len(title.strip()) > 0