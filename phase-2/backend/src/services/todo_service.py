from sqlmodel import Session, select
from src.models.todo import Todo, TodoCreate, TodoUpdate
from typing import List, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TodoService:
    @staticmethod
    def create_todo(session: Session, todo: TodoCreate, user_id: int) -> Todo:
        try:
            logger.info(f"Creating new todo with title: {todo.title} for user ID: {user_id}")
            db_todo = Todo(**todo.model_dump(), user_id=user_id)
            session.add(db_todo)
            session.commit()
            session.refresh(db_todo)
            logger.info(f"Successfully created todo with ID: {db_todo.id} for user ID: {user_id}")
            return db_todo
        except Exception as e:
            logger.error(f"Error creating todo: {str(e)}")
            raise e

    @staticmethod
    def get_todo_by_id(session: Session, todo_id: int, user_id: int) -> Optional[Todo]:
        try:
            logger.info(f"Fetching todo with ID: {todo_id} for user ID: {user_id}")
            # Only return the todo if it belongs to the user
            statement = select(Todo).where(Todo.id == todo_id, Todo.user_id == user_id)
            todo = session.exec(statement).first()
            if todo:
                logger.info(f"Successfully fetched todo with ID: {todo_id} for user ID: {user_id}")
            else:
                logger.warning(f"Todo with ID {todo_id} not found for user ID: {user_id}")
            return todo
        except Exception as e:
            logger.error(f"Error fetching todo with ID {todo_id}: {str(e)}")
            raise e

    @staticmethod
    def get_todos_by_user(session: Session, user_id: int) -> List[Todo]:
        try:
            logger.info(f"Fetching todos for user ID: {user_id}")
            statement = select(Todo).where(Todo.user_id == user_id)
            todos = session.exec(statement).all()
            logger.info(f"Successfully fetched {len(todos)} todos for user ID: {user_id}")
            return todos
        except Exception as e:
            logger.error(f"Error fetching todos for user: {str(e)}")
            raise e

    @staticmethod
    def update_todo(session: Session, todo_id: int, user_id: int, todo_update: TodoUpdate) -> Optional[Todo]:
        try:
            logger.info(f"Updating todo with ID: {todo_id} for user ID: {user_id}")
            # Only update the todo if it belongs to the user
            statement = select(Todo).where(Todo.id == todo_id, Todo.user_id == user_id)
            db_todo = session.exec(statement).first()
            
            if not db_todo:
                logger.warning(f"Todo with ID {todo_id} not found for user ID: {user_id}")
                return None

            todo_data = todo_update.model_dump(exclude_unset=True)
            for key, value in todo_data.items():
                if value is not None:
                    setattr(db_todo, key, value)

            session.add(db_todo)
            session.commit()
            session.refresh(db_todo)
            logger.info(f"Successfully updated todo with ID: {todo_id} for user ID: {user_id}")
            return db_todo
        except Exception as e:
            logger.error(f"Error updating todo with ID {todo_id}: {str(e)}")
            raise e

    @staticmethod
    def delete_todo(session: Session, todo_id: int, user_id: int) -> bool:
        try:
            logger.info(f"Deleting todo with ID: {todo_id} for user ID: {user_id}")
            # Only delete the todo if it belongs to the user
            statement = select(Todo).where(Todo.id == todo_id, Todo.user_id == user_id)
            db_todo = session.exec(statement).first()
            
            if not db_todo:
                logger.warning(f"Todo with ID {todo_id} not found for user ID: {user_id}")
                return False

            session.delete(db_todo)
            session.commit()
            logger.info(f"Successfully deleted todo with ID: {todo_id} for user ID: {user_id}")
            return True
        except Exception as e:
            logger.error(f"Error deleting todo with ID {todo_id}: {str(e)}")
            raise e