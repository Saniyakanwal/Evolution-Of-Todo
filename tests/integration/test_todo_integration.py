"""
Integration tests for the TodoService in the Console-based In-Memory Todo Application.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import pytest
from src.services.todo_service import TodoService
from src.models.task import Task


def test_add_task_integration():
    """Test that adding a task through the service creates a proper task instance."""
    service = TodoService()
    
    task = service.add_task("Integration Test Task")
    
    # Verify the returned task has correct properties
    assert isinstance(task, Task)
    assert task.title == "Integration Test Task"
    assert task.completed is False
    
    # Verify the task was added to the service's internal collection
    assert task.id in service.tasks
    assert service.tasks[task.id] is task


def test_add_and_retrieve_task_integration():
    """Test adding a task and retrieving it through the service."""
    service = TodoService()
    
    added_task = service.add_task("Retrieve Test Task")
    
    retrieved_task = service.get_task_by_id(added_task.id)
    
    assert retrieved_task is not None
    assert retrieved_task.id == added_task.id
    assert retrieved_task.title == added_task.title
    assert retrieved_task.completed == added_task.completed


def test_add_multiple_tasks_integration():
    """Test adding multiple tasks and retrieving them."""
    service = TodoService()
    
    task1 = service.add_task("First Task")
    task2 = service.add_task("Second Task")
    
    all_tasks = service.get_all_tasks()
    
    assert len(all_tasks) == 2
    task_ids = [task.id for task in all_tasks]
    assert task1.id in task_ids
    assert task2.id in task_ids


def test_mark_task_complete_integration():
    """Test marking a task as complete through the service."""
    service = TodoService()
    task = service.add_task("Task to Complete")
    
    result = service.mark_task_complete(task.id)
    
    assert result is True
    assert service.tasks[task.id].completed is True


def test_mark_task_incomplete_integration():
    """Test marking a task as incomplete through the service."""
    service = TodoService()
    task = service.add_task("Task to Mark Incomplete")
    # First mark as complete
    service.mark_task_complete(task.id)
    
    result = service.mark_task_incomplete(task.id)
    
    assert result is True
    assert service.tasks[task.id].completed is False


def test_task_status_toggle_integration():
    """Test toggling task status from incomplete to complete and back."""
    service = TodoService()
    task = service.add_task("Task to Toggle")
    
    # Initial state: incomplete
    assert task.completed is False
    
    # Mark as complete
    service.mark_task_complete(task.id)
    assert service.tasks[task.id].completed is True
    
    # Mark as incomplete again
    service.mark_task_incomplete(task.id)
    assert service.tasks[task.id].completed is False


def test_task_delete_integration():
    """Test deleting a task through the service."""
    service = TodoService()
    task = service.add_task("Task to Delete")
    
    result = service.delete_task(task.id)
    
    assert result is True
    assert len(service.tasks) == 0
    assert task.id not in service.tasks


def test_task_update_integration():
    """Test updating a task's title through the service."""
    service = TodoService()
    task = service.add_task("Original Title")
    
    result = service.update_task(task.id, "New Title")
    
    assert result is True
    assert service.tasks[task.id].title == "New Title"