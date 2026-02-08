from sqlmodel import Session, select
from src.models.todo import Todo, TodoCreate, TodoUpdate
from typing import List, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TodoService:
    @staticmethod
    def create_todo(session: Session, todo: TodoCreate) -> Todo:
        try:
            logger.info(f"Creating new todo with title: {todo.title}")
            db_todo = Todo(**todo.model_dump())
            session.add(db_todo)
            session.commit()
            session.refresh(db_todo)
            logger.info(f"Successfully created todo with ID: {db_todo.id}")
            return db_todo
        except Exception as e:
            logger.error(f"Error creating todo: {str(e)}")
            raise e

    @staticmethod
    def get_todo_by_id(session: Session, todo_id: int) -> Optional[Todo]:
        try:
            logger.info(f"Fetching todo with ID: {todo_id}")
            todo = session.get(Todo, todo_id)
            if todo:
                logger.info(f"Successfully fetched todo with ID: {todo_id}")
            else:
                logger.warning(f"Todo with ID {todo_id} not found")
            return todo
        except Exception as e:
            logger.error(f"Error fetching todo with ID {todo_id}: {str(e)}")
            raise e

    @staticmethod
    def get_all_todos(session: Session) -> List[Todo]:
        try:
            logger.info("Fetching all todos")
            todos = session.exec(select(Todo)).all()
            logger.info(f"Successfully fetched {len(todos)} todos")
            return todos
        except Exception as e:
            logger.error(f"Error fetching all todos: {str(e)}")
            raise e

    @staticmethod
    def update_todo(session: Session, todo_id: int, todo_update: TodoUpdate) -> Optional[Todo]:
        try:
            logger.info(f"Updating todo with ID: {todo_id}")
            db_todo = session.get(Todo, todo_id)
            if not db_todo:
                logger.warning(f"Todo with ID {todo_id} not found for update")
                return None

            todo_data = todo_update.model_dump(exclude_unset=True)
            for key, value in todo_data.items():
                if value is not None:
                    setattr(db_todo, key, value)

            session.add(db_todo)
            session.commit()
            session.refresh(db_todo)
            logger.info(f"Successfully updated todo with ID: {todo_id}")
            return db_todo
        except Exception as e:
            logger.error(f"Error updating todo with ID {todo_id}: {str(e)}")
            raise e

    @staticmethod
    def delete_todo(session: Session, todo_id: int) -> bool:
        try:
            logger.info(f"Deleting todo with ID: {todo_id}")
            db_todo = session.get(Todo, todo_id)
            if not db_todo:
                logger.warning(f"Todo with ID {todo_id} not found for deletion")
                return False

            session.delete(db_todo)
            session.commit()
            logger.info(f"Successfully deleted todo with ID: {todo_id}")
            return True
        except Exception as e:
            logger.error(f"Error deleting todo with ID {todo_id}: {str(e)}")
            raise e