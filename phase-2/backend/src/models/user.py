from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional
import bcrypt


class UserBase(SQLModel):
    username: str = Field(min_length=3, max_length=50, unique=True)
    email: str = Field(min_length=5, max_length=100, unique=True)
    full_name: Optional[str] = Field(default=None, max_length=100)
    bio: Optional[str] = Field(default=None, max_length=500)
    avatar_url: Optional[str] = Field(default=None, max_length=500)


class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = Field(default=True)

    def verify_password(self, plain_password: str) -> bool:
        return bcrypt.checkpw(plain_password.encode('utf-8'), self.hashed_password.encode('utf-8'))


class UserCreate(UserBase):
    password: str

    @property
    def hashed_password(self) -> str:
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(self.password.encode('utf-8'), salt).decode('utf-8')


class UserRead(UserBase):
    id: int
    created_at: datetime


class UserUpdate(SQLModel):
    username: Optional[str] = Field(default=None, min_length=3, max_length=50)
    email: Optional[str] = Field(default=None, min_length=5, max_length=100)
    full_name: Optional[str] = Field(default=None, max_length=100)
    bio: Optional[str] = Field(default=None, max_length=500)
    avatar_url: Optional[str] = Field(default=None, max_length=500)
    password: Optional[str] = Field(default=None, min_length=6)