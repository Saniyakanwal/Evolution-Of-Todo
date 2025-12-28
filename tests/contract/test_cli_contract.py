"""
Contract tests for the Console-based In-Memory Todo Application.

This module tests the CLI contract specifications defined in the contracts/ directory.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import pytest
from src.services.todo_service import TodoService
from src.cli.todo_cli import TodoCLI
import io
import contextlib


def test_add_task_contract():
    """Test the add command contract: 'add \"task title\"' creates a task with unique ID."""
    service = TodoService()
    initial_count = len(service.get_all_tasks())
    
    # Add a task
    task = service.add_task("Test task for contract")
    
    # Verify contract requirements
    assert task is not None, "Task should be returned when added"
    assert task.id is not None, "Task should have a unique ID"
    assert task.id != "", "Task ID should not be empty"
    assert task.title == "Test task for contract", "Task should have the provided title"
    assert task.completed is False, "Task should be marked as incomplete by default"
    assert len(service.get_all_tasks()) == initial_count + 1, "Task count should increase by 1"


def test_delete_task_contract():
    """Test the delete command contract: 'delete <task_id>' removes task."""
    service = TodoService()
    task = service.add_task("Task to delete")
    
    # Verify the task exists before deletion
    assert service.get_task_by_id(task.id) is not None, "Task should exist before deletion"
    
    # Delete the task
    result = service.delete_task(task.id)
    
    # Verify contract requirements
    assert result is True, "Should return True when task is successfully deleted"
    assert service.get_task_by_id(task.id) is None, "Task should no longer exist after deletion"
    

def test_update_task_contract():
    """Test the update command contract: 'update <task_id> \"new title\"' modifies task."""
    service = TodoService()
    task = service.add_task("Original title")
    
    # Update the task
    result = service.update_task(task.id, "Updated title")
    
    # Verify contract requirements
    assert result is True, "Should return True when task is successfully updated"
    updated_task = service.get_task_by_id(task.id)
    assert updated_task.title == "Updated title", "Task title should be updated"


def test_list_tasks_contract():
    """Test the list command contract: 'list' displays all tasks with ID, title, and status."""
    service = TodoService()
    task1 = service.add_task("First task")
    task2 = service.add_task("Second task")
    
    # Get all tasks
    all_tasks = service.get_all_tasks()
    
    # Verify contract requirements
    assert len(all_tasks) == 2, "Should return all tasks"
    task_ids = [task.id for task in all_tasks]
    assert task1.id in task_ids, "First task should be in the list"
    assert task2.id in task_ids, "Second task should be in the list"
    
    # Check for empty list behavior
    for task in all_tasks:
        service.delete_task(task.id)
    
    empty_list = service.get_all_tasks()
    assert len(empty_list) == 0, "Should return empty list when no tasks exist"


def test_mark_complete_contract():
    """Test the complete command contract: 'complete <task_id>' toggles status."""
    service = TodoService()
    task = service.add_task("Task to complete")
    
    # Initially incomplete
    assert task.completed is False, "Task should be incomplete by default"
    
    # Mark as complete
    result = service.mark_task_complete(task.id)
    
    # Verify contract requirements
    assert result is True, "Should return True when task status is changed"
    completed_task = service.get_task_by_id(task.id)
    assert completed_task.completed is True, "Task should be marked as complete"


def test_mark_incomplete_contract():
    """Test the incomplete command contract: 'incomplete <task_id>' toggles status."""
    service = TodoService()
    task = service.add_task("Task to mark incomplete")
    service.mark_task_complete(task.id)  # First mark as complete
    
    # Verify it's complete
    assert service.get_task_by_id(task.id).completed is True, "Task should be complete"
    
    # Mark as incomplete
    result = service.mark_task_incomplete(task.id)
    
    # Verify contract requirements
    assert result is True, "Should return True when task status is changed"
    incomplete_task = service.get_task_by_id(task.id)
    assert incomplete_task.completed is False, "Task should be marked as incomplete"