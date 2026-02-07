import pytest
from fastapi.testclient import TestClient
from backend.src.main import app
from backend.src.models.task import Task
from backend.src.services.task_service import TaskService
from sqlmodel import Session, select
from backend.src.database import engine


client = TestClient(app)


def test_get_all_tasks():
    # Clear any existing tasks
    with Session(engine) as session:
        statement = select(Task)
        tasks = session.exec(statement).all()
        for task in tasks:
            session.delete(task)
        session.commit()

    # Create some test tasks
    response = client.post("/api/v1/tasks", json={
        "title": "Test Task 1",
        "description": "Test Description 1",
        "status": "pending"
    })
    assert response.status_code == 201

    response = client.post("/api/v1/tasks", json={
        "title": "Test Task 2",
        "description": "Test Description 2",
        "status": "completed"
    })
    assert response.status_code == 201

    # Get all tasks
    response = client.get("/api/v1/tasks")
    assert response.status_code == 200

    data = response.json()
    assert len(data) == 2

    # Check that the tasks have the expected properties
    task1 = data[0]
    assert "id" in task1
    assert task1["title"] == "Test Task 1"
    assert task1["description"] == "Test Description 1"
    assert task1["status"] == "pending"
    assert "created_at" in task1

    task2 = data[1]
    assert "id" in task2
    assert task2["title"] == "Test Task 2"
    assert task2["description"] == "Test Description 2"
    assert task2["status"] == "completed"
    assert "created_at" in task2


def test_create_task():
    # Test creating a new task
    response = client.post("/api/v1/tasks", json={
        "title": "New Test Task",
        "description": "New Test Description",
        "status": "pending"
    })
    
    assert response.status_code == 201
    
    data = response.json()
    assert "id" in data
    assert data["title"] == "New Test Task"
    assert data["description"] == "New Test Description"
    assert data["status"] == "pending"
    assert "created_at" in data


def test_create_task_with_minimal_data():
    # Test creating a task with only required fields
    response = client.post("/api/v1/tasks", json={
        "title": "Minimal Task"
    })
    
    assert response.status_code == 201
    
    data = response.json()
    assert "id" in data
    assert data["title"] == "Minimal Task"
    assert data["description"] is None
    assert data["status"] == "pending"
    assert "created_at" in data


def test_create_task_with_invalid_data():
    # Test creating a task with invalid data
    response = client.post("/api/v1/tasks", json={
        "title": "",  # Empty title should fail validation
        "status": "pending"
    })
    
    assert response.status_code == 422  # Validation error


def test_create_task_with_invalid_status():
    # Test creating a task with invalid status
    response = client.post("/api/v1/tasks", json={
        "title": "Invalid Status Task",
        "status": "invalid_status"  # Invalid status should fail validation
    })

    assert response.status_code == 422  # Validation error


def test_update_task():
    # First create a task
    create_response = client.post("/api/v1/tasks", json={
        "title": "Original Task",
        "description": "Original Description",
        "status": "pending"
    })
    assert create_response.status_code == 201
    task_id = create_response.json()["id"]

    # Update the task
    update_response = client.put(f"/api/v1/tasks/{task_id}", json={
        "title": "Updated Task",
        "description": "Updated Description",
        "status": "completed"
    })

    assert update_response.status_code == 200

    updated_data = update_response.json()
    assert updated_data["id"] == task_id
    assert updated_data["title"] == "Updated Task"
    assert updated_data["description"] == "Updated Description"
    assert updated_data["status"] == "completed"


def test_update_task_partial():
    # First create a task
    create_response = client.post("/api/v1/tasks", json={
        "title": "Original Task",
        "description": "Original Description",
        "status": "pending"
    })
    assert create_response.status_code == 201
    task_id = create_response.json()["id"]

    # Update only the status
    update_response = client.put(f"/api/v1/tasks/{task_id}", json={
        "status": "completed"
    })

    assert update_response.status_code == 200

    updated_data = update_response.json()
    assert updated_data["id"] == task_id
    assert updated_data["title"] == "Original Task"  # Unchanged
    assert updated_data["description"] == "Original Description"  # Unchanged
    assert updated_data["status"] == "completed"  # Updated


def test_update_nonexistent_task():
    # Try to update a task that doesn't exist
    update_response = client.put("/api/v1/tasks/999999", json={
        "title": "Updated Task",
        "status": "completed"
    })

    assert update_response.status_code == 404


def test_delete_task():
    # First create a task
    create_response = client.post("/api/v1/tasks", json={
        "title": "Task to Delete",
        "description": "Description to Delete",
        "status": "pending"
    })
    assert create_response.status_code == 201
    task_id = create_response.json()["id"]

    # Verify the task exists
    get_response = client.get(f"/api/v1/tasks/{task_id}")
    assert get_response.status_code == 200

    # Delete the task
    delete_response = client.delete(f"/api/v1/tasks/{task_id}")
    assert delete_response.status_code == 204

    # Verify the task is gone
    get_response = client.get(f"/api/v1/tasks/{task_id}")
    assert get_response.status_code == 404


def test_delete_nonexistent_task():
    # Try to delete a task that doesn't exist
    delete_response = client.delete("/api/v1/tasks/999999")
    assert delete_response.status_code == 404