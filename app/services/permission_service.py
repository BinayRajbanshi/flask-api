from typing import List, Optional
from app import db
from app.models.permission import Permission
from sqlalchemy.exc import SQLAlchemyError


class permissionService:
    
    
    @staticmethod
    def get_all_permissions() -> List[Permission]:
        try:
            return Permission.query.order_by(Permission.created_at.desc()).all()
        except SQLAlchemyError:
            return []
    
    @staticmethod
    def get_permission_by_id(permission_id: int) -> Optional[Permission]:
        try:
            return Permission.query.get(permission_id)
        except SQLAlchemyError:
            return None
