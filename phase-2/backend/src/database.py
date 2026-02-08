from sqlalchemy import create_engine
from sqlmodel import Session
from .config import DATABASE_URL
from src.models.todo import Todo
from src.models.user import User


# Create the database engine
engine = create_engine(DATABASE_URL, echo=True)


def create_db_and_tables():
    Todo.metadata.create_all(bind=engine)
    User.metadata.create_all(bind=engine)


def get_session():
    with Session(engine) as session:
        yield session