from fastapi import APIRouter, Depends, HTTPException, Request
from sqlmodel import Session
from typing import List
import logging

from ..database import get_session
from ..models.user import User, UserCreate, UserUpdate, UserRead
from ..services.user_service import UserService

router = APIRouter()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@router.post("/users", response_model=UserRead)
async def create_user(user: UserCreate, session: Session = Depends(get_session)):
    logger.info(f"Creating new user with email: {user.email}")
    try:
        # Check if user with this email already exists
        existing_user = UserService.get_user_by_email(session, user.email)
        if existing_user:
            logger.warning(f"Attempt to register with existing email: {user.email}")
            raise HTTPException(status_code=400, detail="Email already registered")

        # Check if username already exists
        existing_username = UserService.get_user_by_username(session, user.username)
        if existing_username:
            logger.warning(f"Attempt to register with existing username: {user.username}")
            raise HTTPException(status_code=400, detail="Username already taken")

        created_user = UserService.create_user(session, user)
        logger.info(f"Successfully created user with ID: {created_user.id}")
        return created_user
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error creating user: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/users/{user_id}", response_model=UserRead)
async def get_user(user_id: int, session: Session = Depends(get_session)):
    logger.info(f"Fetching user with ID: {user_id}")
    try:
        user = UserService.get_user_by_id(session, user_id)
        if not user:
            logger.warning(f"User with ID {user_id} not found")
            raise HTTPException(status_code=404, detail="User not found")
        logger.info(f"Successfully fetched user with ID: {user_id}")
        return user
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching user: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.patch("/users/{user_id}", response_model=UserRead)
async def update_user(
    user_id: int,
    user_update: UserUpdate,
    session: Session = Depends(get_session)
):
    logger.info(f"Updating user with ID: {user_id}")
    try:
        user = UserService.update_user(session, user_id, user_update)
        if not user:
            logger.warning(f"User with ID {user_id} not found for update")
            raise HTTPException(status_code=404, detail="User not found")
        logger.info(f"Successfully updated user with ID: {user_id}")
        return user
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error updating user: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.delete("/users/{user_id}")
async def delete_user(user_id: int, session: Session = Depends(get_session)):
    logger.info(f"Deleting user with ID: {user_id}")
    try:
        success = UserService.delete_user(session, user_id)
        if not success:
            logger.warning(f"User with ID {user_id} not found for deletion")
            raise HTTPException(status_code=404, detail="User not found")
        logger.info(f"Successfully deleted user with ID: {user_id}")
        return {"success": True}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error deleting user: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post("/auth/login")
async def login(request: Request, session: Session = Depends(get_session)):
    try:
        # Get JSON data from request
        json_data = await request.json()
        email = json_data.get("email")
        password = json_data.get("password")
        
        logger.info(f"Login attempt for email: {email}")
        
        if not email or not password:
            logger.warning(f"Missing email or password in login request")
            raise HTTPException(status_code=400, detail="Email and password are required")
        
        user = UserService.authenticate_user(session, email, password)
        if not user:
            logger.warning(f"Invalid credentials for email: {email}")
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        logger.info(f"Successful login for user ID: {user.id}")
        return {
            "access_token": str(user.id), 
            "token_type": "bearer", 
            "user_id": user.id, 
            "username": user.username
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error during login: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")