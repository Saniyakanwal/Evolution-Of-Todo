"""
Unit tests for the Task model in the Console-based In-Memory Todo Application.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import pytest
from src.models.task import Task


def test_task_creation_with_defaults():
    """Test that a Task can be created with default values."""
    task_id = "test-id-123"
    task_title = "Test Task"
    
    task = Task(id=task_id, title=task_title)
    
    assert task.id == task_id
    assert task.title == task_title
    assert task.completed is False  # Default value


def test_task_creation_with_completed_status():
    """Test that a Task can be created with completed status set to True."""
    task_id = "test-id-456"
    task_title = "Completed Task"
    
    task = Task(id=task_id, title=task_title, completed=True)
    
    assert task.id == task_id
    assert task.title == task_title
    assert task.completed is True


def test_task_creation_fails_with_empty_id():
    """Test that creating a Task with an empty ID raises ValueError."""
    with pytest.raises(ValueError, match="Task ID cannot be empty"):
        Task(id="", title="Test Task")


def test_task_creation_fails_with_empty_title():
    """Test that creating a Task with an empty title raises ValueError."""
    with pytest.raises(ValueError, match="Task title cannot be empty"):
        Task(id="test-id-789", title="")


def test_task_creation_fails_with_none_title():
    """Test that creating a Task with a None title raises ValueError."""
    with pytest.raises(ValueError, match="Task title cannot be empty"):
        Task(id="test-id-000", title=None)