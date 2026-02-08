from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List
import logging

from ..database import get_session
from ..models.todo import Todo, TodoCreate, TodoUpdate
from ..services.todo_service import TodoService

router = APIRouter()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@router.get("/todos", response_model=List[Todo])
async def get_todos(session: Session = Depends(get_session)):
    logger.info("Fetching all todos")
    try:
        todos = TodoService.get_all_todos(session)
        logger.info(f"Successfully fetched {len(todos)} todos")
        return todos
    except Exception as e:
        logger.error(f"Error fetching todos: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post("/todos", response_model=Todo)
async def create_todo(todo: TodoCreate, session: Session = Depends(get_session)):
    logger.info(f"Creating new todo with title: {todo.title}")
    try:
        created_todo = TodoService.create_todo(session, todo)
        logger.info(f"Successfully created todo with ID: {created_todo.id}")
        return created_todo
    except Exception as e:
        logger.error(f"Error creating todo: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.patch("/todos/{todo_id}", response_model=Todo)
async def update_todo(
    todo_id: int,
    todo_update: TodoUpdate,
    session: Session = Depends(get_session)
):
    logger.info(f"Updating todo with ID: {todo_id}")
    try:
        todo = TodoService.update_todo(session, todo_id, todo_update)
        if not todo:
            logger.warning(f"Todo with ID {todo_id} not found for update")
            raise HTTPException(status_code=404, detail="Todo not found")
        logger.info(f"Successfully updated todo with ID: {todo_id}")
        return todo
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error updating todo: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int, session: Session = Depends(get_session)):
    logger.info(f"Deleting todo with ID: {todo_id}")
    try:
        success = TodoService.delete_todo(session, todo_id)
        if not success:
            logger.warning(f"Todo with ID {todo_id} not found for deletion")
            raise HTTPException(status_code=404, detail="Todo not found")
        logger.info(f"Successfully deleted todo with ID: {todo_id}")
        return {"success": True}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error deleting todo: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")