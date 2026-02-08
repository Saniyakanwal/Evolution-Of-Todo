import pytest
from fastapi.testclient import TestClient
from backend.src.main import app
from backend.src.models.task import Task
from sqlmodel import Session, select
from backend.src.database import engine


client = TestClient(app)


def test_create_task_integration():
    # Test the full flow of creating a task and then retrieving it
    # First, clear any existing tasks
    with Session(engine) as session:
        tasks = session.exec(select(Task)).all()
        for task in tasks:
            session.delete(task)
        session.commit()
    
    # Create a new task via the API
    create_response = client.post("/api/v1/tasks", json={
        "title": "Integration Test Task",
        "description": "Integration Test Description",
        "status": "pending"
    })
    
    assert create_response.status_code == 201
    created_task = create_response.json()
    assert "id" in created_task
    task_id = created_task["id"]
    
    # Retrieve the task via the API
    get_response = client.get(f"/api/v1/tasks/{task_id}")
    assert get_response.status_code == 200
    
    retrieved_task = get_response.json()
    assert retrieved_task["id"] == task_id
    assert retrieved_task["title"] == "Integration Test Task"
    assert retrieved_task["description"] == "Integration Test Description"
    assert retrieved_task["status"] == "pending"
    assert "created_at" in retrieved_task


def test_task_lifecycle():
    # Test the full lifecycle: create, read, update, delete
    # Clear any existing tasks
    with Session(engine) as session:
        tasks = session.exec(select(Task)).all()
        for task in tasks:
            session.delete(task)
        session.commit()
    
    # 1. Create a task
    create_response = client.post("/api/v1/tasks", json={
        "title": "Lifecycle Test Task",
        "description": "Original description",
        "status": "pending"
    })
    assert create_response.status_code == 201
    created_task = create_response.json()
    assert "id" in created_task
    task_id = created_task["id"]
    
    # 2. Read the task
    get_response = client.get(f"/api/v1/tasks/{task_id}")
    assert get_response.status_code == 200
    retrieved_task = get_response.json()
    assert retrieved_task["title"] == "Lifecycle Test Task"
    assert retrieved_task["description"] == "Original description"
    assert retrieved_task["status"] == "pending"
    
    # 3. Update the task
    update_response = client.put(f"/api/v1/tasks/{task_id}", json={
        "title": "Updated Lifecycle Test Task",
        "description": "Updated description",
        "status": "completed"
    })
    assert update_response.status_code == 200
    updated_task = update_response.json()
    assert updated_task["title"] == "Updated Lifecycle Test Task"
    assert updated_task["description"] == "Updated description"
    assert updated_task["status"] == "completed"
    
    # 4. Verify the update by reading again
    get_response = client.get(f"/api/v1/tasks/{task_id}")
    assert get_response.status_code == 200
    verified_task = get_response.json()
    assert verified_task["title"] == "Updated Lifecycle Test Task"
    assert verified_task["description"] == "Updated description"
    assert verified_task["status"] == "completed"
    
    # 5. Delete the task
    delete_response = client.delete(f"/api/v1/tasks/{task_id}")
    assert delete_response.status_code == 204
    
    # 6. Verify the task is deleted
    get_deleted_response = client.get(f"/api/v1/tasks/{task_id}")
    assert get_deleted_response.status_code == 404