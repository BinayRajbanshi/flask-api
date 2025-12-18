from typing import List, Optional
from app import db
from app.models.user import User
from sqlalchemy.exc import SQLAlchemyError


class UserService:
    @staticmethod
    def create_user(username: str, email: str, password:str):
        try:
            user = User(username=username, email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            return user, None
        except SQLAlchemyError as e:
            db.session.rollback()
            return None, f"Database error: {str(e)}"
        except Exception as e:
            db.session.rollback()
            return None, f"Unexpected error: {str(e)}"
    
    @staticmethod
    def get_all_users() -> List[User]:
        try:
            return User.query.order_by(User.created_at.desc()).all()
        except SQLAlchemyError:
            return []
    
    @staticmethod
    def get_user_by_id(user_id: int) -> Optional[User]:
        try:
            return User.query.get(user_id)
        except SQLAlchemyError:
            return None
    
    # @staticmethod
    # def update_todo(User: User, title: Optional[str] = None, completed: Optional[bool] = None) -> tuple[bool, Optional[str]]:
    #     try:
    #         if title is not None:
    #             todo.title = title
    #         if completed is not None:
    #             todo.completed = completed
            
    #         db.session.commit()
    #         return True, None
    #     except SQLAlchemyError as e:
    #         db.session.rollback()
    #         return False, f"Database error: {str(e)}"
    #     except Exception as e:
    #         db.session.rollback()
    #         return False, f"Unexpected error: {str(e)}"
    
    @staticmethod
    def delete_user(user: User):
        try:
            db.session.delete(user)
            db.session.commit()
            return True, None
        except SQLAlchemyError as e:
            db.session.rollback()
            return False, f"Database error: {str(e)}"
        except Exception as e:
            db.session.rollback()
            return False, f"Unexpected error: {str(e)}"

