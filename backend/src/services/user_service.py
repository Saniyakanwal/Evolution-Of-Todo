from sqlmodel import Session, select
from src.models.user import User, UserCreate, UserUpdate
from typing import List, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class UserService:
    @staticmethod
    def create_user(session: Session, user: UserCreate) -> User:
        try:
            logger.info(f"Creating new user with email: {user.email}")
            # Hash the password
            import bcrypt
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), salt).decode('utf-8')

            db_user = User(**user.model_dump(exclude={'password'}), hashed_password=hashed_password)
            session.add(db_user)
            session.commit()
            session.refresh(db_user)
            logger.info(f"Successfully created user with ID: {db_user.id}")
            return db_user
        except Exception as e:
            logger.error(f"Error creating user: {str(e)}")
            raise e

    @staticmethod
    def get_user_by_id(session: Session, user_id: int) -> Optional[User]:
        try:
            logger.info(f"Fetching user with ID: {user_id}")
            user = session.get(User, user_id)
            if user:
                logger.info(f"Successfully fetched user with ID: {user_id}")
            else:
                logger.warning(f"User with ID {user_id} not found")
            return user
        except Exception as e:
            logger.error(f"Error fetching user with ID {user_id}: {str(e)}")
            raise e

    @staticmethod
    def get_user_by_email(session: Session, email: str) -> Optional[User]:
        try:
            logger.info(f"Fetching user with email: {email}")
            statement = select(User).where(User.email == email)
            user = session.exec(statement).first()
            if user:
                logger.info(f"Successfully fetched user with email: {email}")
            else:
                logger.warning(f"User with email {email} not found")
            return user
        except Exception as e:
            logger.error(f"Error fetching user with email {email}: {str(e)}")
            raise e

    @staticmethod
    def get_user_by_username(session: Session, username: str) -> Optional[User]:
        try:
            logger.info(f"Fetching user with username: {username}")
            statement = select(User).where(User.username == username)
            user = session.exec(statement).first()
            if user:
                logger.info(f"Successfully fetched user with username: {username}")
            else:
                logger.warning(f"User with username {username} not found")
            return user
        except Exception as e:
            logger.error(f"Error fetching user with username {username}: {str(e)}")
            raise e

    @staticmethod
    def get_all_users(session: Session) -> List[User]:
        try:
            logger.info("Fetching all users")
            users = session.exec(select(User)).all()
            logger.info(f"Successfully fetched {len(users)} users")
            return users
        except Exception as e:
            logger.error(f"Error fetching all users: {str(e)}")
            raise e

    @staticmethod
    def update_user(session: Session, user_id: int, user_update: UserUpdate) -> Optional[User]:
        try:
            logger.info(f"Updating user with ID: {user_id}")
            db_user = session.get(User, user_id)
            if not db_user:
                logger.warning(f"User with ID {user_id} not found for update")
                return None

            user_data = user_update.model_dump(exclude_unset=True)
            if 'password' in user_data and user_data['password']:
                # Hash the new password
                import bcrypt
                salt = bcrypt.gensalt()
                user_data['hashed_password'] = bcrypt.hashpw(
                    user_data['password'].encode('utf-8'), salt
                ).decode('utf-8')
                del user_data['password']  # Remove plain password from update data

            for key, value in user_data.items():
                if value is not None:
                    setattr(db_user, key, value)

            session.add(db_user)
            session.commit()
            session.refresh(db_user)
            logger.info(f"Successfully updated user with ID: {user_id}")
            return db_user
        except Exception as e:
            logger.error(f"Error updating user with ID {user_id}: {str(e)}")
            raise e

    @staticmethod
    def delete_user(session: Session, user_id: int) -> bool:
        try:
            logger.info(f"Deleting user with ID: {user_id}")
            db_user = session.get(User, user_id)
            if not db_user:
                logger.warning(f"User with ID {user_id} not found for deletion")
                return False

            session.delete(db_user)
            session.commit()
            logger.info(f"Successfully deleted user with ID: {user_id}")
            return True
        except Exception as e:
            logger.error(f"Error deleting user with ID {user_id}: {str(e)}")
            raise e

    @staticmethod
    def authenticate_user(session: Session, email: str, password: str) -> Optional[User]:
        try:
            logger.info(f"Authenticating user with email: {email}")
            user = UserService.get_user_by_email(session, email)
            if not user or not user.verify_password(password):
                logger.warning(f"Authentication failed for email: {email}")
                return None
            logger.info(f"Successfully authenticated user with ID: {user.id}")
            return user
        except Exception as e:
            logger.error(f"Error authenticating user with email {email}: {str(e)}")
            raise e