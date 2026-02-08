from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from src.database import get_session
from src.models.task import Task, TaskCreate, TaskRead, TaskUpdate
from src.services.task_service import TaskService
from typing import List

router = APIRouter()


@router.post("/tasks", response_model=TaskRead, status_code=201)
def create_task(task: TaskCreate, session: Session = Depends(get_session)) -> Task:
    return TaskService.create_task(session, task)


@router.get("/tasks", response_model=List[TaskRead])
def read_tasks(session: Session = Depends(get_session)) -> List[Task]:
    return TaskService.get_all_tasks(session)


@router.get("/tasks/{task_id}", response_model=TaskRead)
def read_task(task_id: int, session: Session = Depends(get_session)) -> Task:
    task = TaskService.get_task_by_id(session, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.put("/tasks/{task_id}", response_model=TaskRead)
def update_task(task_id: int, task_update: TaskUpdate, session: Session = Depends(get_session)) -> Task:
    task = TaskService.update_task(session, task_id, task_update)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int, session: Session = Depends(get_session)):
    success = TaskService.delete_task(session, task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return