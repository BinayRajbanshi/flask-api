from typing import List, Optional
from app import db
from app.models.group import Group
from sqlalchemy.exc import SQLAlchemyError


class GroupService:
    @staticmethod
    def create_group(name: str) -> tuple[Optional[Group], Optional[str]]:
        try:
            group = Group(name=name)
            db.session.add(group)
            db.session.commit()
            return group, None
        except SQLAlchemyError as e:
            db.session.rollback()
            return None, f"Database error: {str(e)}"
        except Exception as e:
            db.session.rollback()
            return None, f"Unexpected error: {str(e)}"
    
    @staticmethod
    def get_all_groups() -> List[Group]:
        try:
            return Group.query.order_by(Group.created_at.desc()).all()
        except SQLAlchemyError:
            return []
    
    @staticmethod
    def get_group_by_id(group_id: int) -> Optional[Group]:
        try:
            return Group.query.get(group_id)
        except SQLAlchemyError:
            return None
    
    @staticmethod
    def update_group(group: Group, title: Optional[str] = None, completed: Optional[bool] = None) -> tuple[bool, Optional[str]]:
        try:
            if title is not None:
                group.title = title
            if completed is not None:
                group.completed = completed
            
            db.session.commit()
            return True, None
        except SQLAlchemyError as e:
            db.session.rollback()
            return False, f"Database error: {str(e)}"
        except Exception as e:
            db.session.rollback()
            return False, f"Unexpected error: {str(e)}"
    
    @staticmethod
    def delete_group(group: Group) -> tuple[bool, Optional[str]]:
        try:
            db.session.delete(group)
            db.session.commit()
            return True, None
        except SQLAlchemyError as e:
            db.session.rollback()
            return False, f"Database error: {str(e)}"
        except Exception as e:
            db.session.rollback()
            return False, f"Unexpected error: {str(e)}"

