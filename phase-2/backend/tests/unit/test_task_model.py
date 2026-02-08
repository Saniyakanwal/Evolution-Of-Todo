import pytest
from backend.src.models.task import Task, TaskCreate, TaskUpdate
from datetime import datetime


def test_task_creation():
    # Test creating a task with required fields only
    task_data = {
        "title": "Test Task",
        "description": "Test Description",
        "status": "pending"
    }
    
    task = TaskCreate(**task_data)
    assert task.title == "Test Task"
    assert task.description == "Test Description"
    assert task.status == "pending"


def test_task_with_defaults():
    # Test creating a task without optional fields
    task_data = {
        "title": "Test Task",
    }
    
    task = TaskCreate(**task_data)
    assert task.title == "Test Task"
    assert task.description is None
    assert task.status == "pending"  # Default value


def test_task_update():
    # Test updating a task with partial data
    update_data = {
        "title": "Updated Task",
        "status": "completed"
    }
    
    task_update = TaskUpdate(**update_data)
    assert task_update.title == "Updated Task"
    assert task_update.status == "completed"
    assert task_update.description is None  # Not provided, so None


def test_task_validation():
    # Test validation for title length
    with pytest.raises(ValueError):
        TaskCreate(title="")  # Title too short
    
    # Test validation for status
    with pytest.raises(ValueError):
        TaskCreate(title="Test Task", status="invalid_status")  # Invalid status