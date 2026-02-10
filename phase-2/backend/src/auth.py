from fastapi import Depends, HTTPException, status
from sqlmodel import Session
from src.database import get_session
from src.services.user_service import UserService
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    session: Session = Depends(get_session)
):
    """
    Dependency to get the current authenticated user based on the token.
    In this implementation, the token is the user ID as a string.
    """
    try:
        # Extract the token (which is the user ID)
        token = credentials.credentials
        
        # Convert the token to an integer (user ID)
        user_id = int(token)
        
        # Get the user from the database
        user = UserService.get_user_by_id(session, user_id)
        
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        return user
    except ValueError:
        # If the token is not a valid integer
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )