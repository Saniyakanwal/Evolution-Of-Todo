from sqlalchemy import create_engine
from sqlmodel import Session
from .config import DATABASE_URL
from src.models.todo import Todo
from src.models.user import User
from sqlalchemy import text


# Create the database engine
engine = create_engine(DATABASE_URL, echo=True)


def create_db_and_tables():
    # Create all tables
    User.metadata.create_all(bind=engine)
    
    # Create Todo table with the new schema
    Todo.metadata.create_all(bind=engine)
    
    # Check if the todo table exists and if it has data but no user_id values
    with engine.connect() as conn:
        # Check if there are any todos without a user_id
        result = conn.execute(text("SELECT COUNT(*) FROM todo WHERE user_id IS NULL"))
        todos_without_user = result.fetchone()[0]
        
        # If there are todos without user_id, assign them to a default user (e.g., user_id = 1)
        if todos_without_user > 0:
            conn.execute(text("UPDATE todo SET user_id = 1 WHERE user_id IS NULL"))
            conn.commit()


def get_session():
    with Session(engine) as session:
        yield session