from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional
from enum import Enum
from sqlalchemy import ForeignKey


class StatusEnum(str, Enum):
    pending = "pending"
    completed = "completed"


class TodoBase(SQLModel):
    title: str = Field(min_length=1, max_length=200)
    description: Optional[str] = Field(default=None, max_length=1000)
    status: StatusEnum = Field(default=StatusEnum.pending)


class Todo(TodoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(default=None, foreign_key="user.id")  # Foreign key to user
    created_at: datetime = Field(default_factory=datetime.utcnow)


class TodoCreate(TodoBase):
    pass


class TodoRead(TodoBase):
    id: int
    user_id: int
    created_at: datetime


class TodoUpdate(SQLModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=200)
    description: Optional[str] = Field(default=None, max_length=1000)
    status: Optional[StatusEnum] = Field(default=None)