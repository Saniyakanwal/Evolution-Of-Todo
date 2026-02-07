"""
Unit tests for the TodoService in the Console-based In-Memory Todo Application.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import pytest
from src.services.todo_service import TodoService
from src.models.task import Task


def test_add_task_creates_task_with_unique_id():
    """Test that add_task creates a new task with a unique ID and default incomplete status."""
    service = TodoService()
    
    task = service.add_task("Test Task")
    
    assert isinstance(task, Task)
    assert task.id is not None
    assert task.id != ""
    assert task.title == "Test Task"
    assert task.completed is False


def test_add_task_with_empty_title_raises_error():
    """Test that add_task raises ValueError when given an empty title."""
    service = TodoService()
    
    with pytest.raises(ValueError, match="Task title cannot be empty"):
        service.add_task("")


def test_add_task_with_none_title_raises_error():
    """Test that add_task raises ValueError when given a None title."""
    service = TodoService()
    
    with pytest.raises(ValueError, match="Task title cannot be empty"):
        service.add_task(None)


def test_add_task_adds_to_internal_collection():
    """Test that add_task adds the task to the internal collection."""
    service = TodoService()
    
    task = service.add_task("Test Task")
    
    assert task.id in service.tasks
    assert service.tasks[task.id] == task
    assert len(service.tasks) == 1


def test_get_all_tasks_initially_empty():
    """Test that get_all_tasks returns an empty list when no tasks exist."""
    service = TodoService()
    
    tasks = service.get_all_tasks()
    
    assert len(tasks) == 0


def test_get_all_tasks_returns_all_tasks():
    """Test that get_all_tasks returns all added tasks."""
    service = TodoService()
    
    service.add_task("Task 1")
    service.add_task("Task 2")
    
    tasks = service.get_all_tasks()
    
    assert len(tasks) == 2


def test_mark_task_complete():
    """Test that mark_task_complete marks a task as complete."""
    service = TodoService()
    task = service.add_task("Test Task")
    
    result = service.mark_task_complete(task.id)
    
    assert result is True
    assert service.tasks[task.id].completed is True


def test_mark_task_complete_returns_false_for_nonexistent_task():
    """Test that mark_task_complete returns False for a nonexistent task."""
    service = TodoService()
    
    result = service.mark_task_complete("nonexistent-id")
    
    assert result is False


def test_mark_task_incomplete():
    """Test that mark_task_incomplete marks a task as incomplete."""
    service = TodoService()
    task = service.add_task("Test Task")
    # First mark as complete
    service.mark_task_complete(task.id)
    # Then mark as incomplete
    result = service.mark_task_incomplete(task.id)
    
    assert result is True
    assert service.tasks[task.id].completed is False


def test_mark_task_incomplete_returns_false_for_nonexistent_task():
    """Test that mark_task_incomplete returns False for a nonexistent task."""
    service = TodoService()
    
    result = service.mark_task_incomplete("nonexistent-id")
    
    assert result is False


def test_delete_task():
    """Test that delete_task removes a task from the collection."""
    service = TodoService()
    task = service.add_task("Test Task")
    
    result = service.delete_task(task.id)
    
    assert result is True
    assert task.id not in service.tasks
    assert len(service.tasks) == 0


def test_delete_task_returns_false_for_nonexistent_task():
    """Test that delete_task returns False for a nonexistent task."""
    service = TodoService()
    
    result = service.delete_task("nonexistent-id")
    
    assert result is False


def test_update_task():
    """Test that update_task updates the title of an existing task."""
    service = TodoService()
    task = service.add_task("Original Task")
    
    result = service.update_task(task.id, "Updated Task")
    
    assert result is True
    assert service.tasks[task.id].title == "Updated Task"


def test_update_task_returns_false_for_nonexistent_task():
    """Test that update_task returns False for a nonexistent task."""
    service = TodoService()
    
    result = service.update_task("nonexistent-id", "New Title")
    
    assert result is False


def test_update_task_with_empty_title_raises_error():
    """Test that update_task raises ValueError when given an empty title for existing task."""
    service = TodoService()
    task = service.add_task("Original Task")
    
    with pytest.raises(ValueError, match="Task title cannot be empty"):
        service.update_task(task.id, "")


def test_get_task_by_id():
    """Test that get_task_by_id returns the correct task."""
    service = TodoService()
    task = service.add_task("Test Task")
    
    retrieved_task = service.get_task_by_id(task.id)
    
    assert retrieved_task == task


def test_get_task_by_id_returns_none_for_nonexistent_task():
    """Test that get_task_by_id returns None for a nonexistent task."""
    service = TodoService()
    
    retrieved_task = service.get_task_by_id("nonexistent-id")
    
    assert retrieved_task is None