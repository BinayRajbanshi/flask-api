from flask import request
from typing import Tuple
from marshmallow import ValidationError

from app.services.permission_service import permissionService
from app.utils.response import success_response, error_response

class PermissionController:    
    @staticmethod
    def get_all_permissions() -> Tuple:
        permissions = permissionService.get_all_permissions()
        permissions_data = [permission.to_dict() for permission in permissions]
        return success_response(permissions_data, "permissions retrieved successfully")
    
    @staticmethod
    def get_permission_by_id(permission_id: int) -> Tuple:
        permission = permissionService.get_permission_by_id(permission_id)
        
        if not permission:
            return error_response("permission not found", 404)
        
        return success_response(permission.to_dict(), "permission retrieved successfully")
    