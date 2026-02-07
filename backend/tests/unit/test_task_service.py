import pytest
from backend.src.services.task_service import TaskService
from backend.src.models.task import TaskCreate, TaskUpdate
from sqlmodel import Session, select
from backend.src.database import engine
from backend.src.models.task import Task


def test_task_service_create():
    # Clear any existing tasks
    with Session(engine) as session:
        tasks = session.exec(select(Task)).all()
        for task in tasks:
            session.delete(task)
        session.commit()
    
    # Create a task using the service
    task_create = TaskCreate(
        title="Service Test Task",
        description="Service Test Description",
        status="pending"
    )
    
    created_task = TaskService.create_task(Session(engine), task_create)
    
    assert created_task.title == "Service Test Task"
    assert created_task.description == "Service Test Description"
    assert created_task.status == "pending"
    assert created_task.id is not None


def test_task_service_get_by_id():
    # Create a task first
    task_create = TaskCreate(
        title="Get Test Task",
        description="Get Test Description",
        status="pending"
    )
    
    created_task = TaskService.create_task(Session(engine), task_create)
    task_id = created_task.id
    
    # Retrieve the task using the service
    retrieved_task = TaskService.get_task_by_id(Session(engine), task_id)
    
    assert retrieved_task is not None
    assert retrieved_task.id == task_id
    assert retrieved_task.title == "Get Test Task"


def test_task_service_get_all():
    # Clear any existing tasks
    with Session(engine) as session:
        tasks = session.exec(select(Task)).all()
        for task in tasks:
            session.delete(task)
        session.commit()
    
    # Create multiple tasks
    task_create_1 = TaskCreate(title="All Test 1", description="Desc 1", status="pending")
    task_create_2 = TaskCreate(title="All Test 2", description="Desc 2", status="completed")
    
    TaskService.create_task(Session(engine), task_create_1)
    TaskService.create_task(Session(engine), task_create_2)
    
    # Get all tasks using the service
    all_tasks = TaskService.get_all_tasks(Session(engine))
    
    assert len(all_tasks) == 2
    titles = [task.title for task in all_tasks]
    assert "All Test 1" in titles
    assert "All Test 2" in titles


def test_task_service_update():
    # Create a task first
    task_create = TaskCreate(
        title="Update Original",
        description="Update Original Desc",
        status="pending"
    )
    
    created_task = TaskService.create_task(Session(engine), task_create)
    task_id = created_task.id
    
    # Update the task using the service
    task_update = TaskUpdate(
        title="Update New",
        description="Update New Desc",
        status="completed"
    )
    
    updated_task = TaskService.update_task(Session(engine), task_id, task_update)
    
    assert updated_task is not None
    assert updated_task.id == task_id
    assert updated_task.title == "Update New"
    assert updated_task.description == "Update New Desc"
    assert updated_task.status == "completed"


def test_task_service_delete():
    # Create a task first
    task_create = TaskCreate(
        title="Delete Test",
        description="Delete Test Desc",
        status="pending"
    )
    
    created_task = TaskService.create_task(Session(engine), task_create)
    task_id = created_task.id
    
    # Verify the task exists
    retrieved_task = TaskService.get_task_by_id(Session(engine), task_id)
    assert retrieved_task is not None
    
    # Delete the task using the service
    success = TaskService.delete_task(Session(engine), task_id)
    assert success is True
    
    # Verify the task is gone
    retrieved_task = TaskService.get_task_by_id(Session(engine), task_id)
    assert retrieved_task is None


def test_task_service_delete_nonexistent():
    # Try to delete a task that doesn't exist
    success = TaskService.delete_task(Session(engine), 999999)
    assert success is False