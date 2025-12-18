from flask import request
from typing import Tuple
from marshmallow import ValidationError

from app.services.group_service import GroupService
from app.schemas.group_schema import GroupCreateschema
from app.utils.response import success_response, error_response

class GroupController:
    @staticmethod
    def create_group() -> Tuple:
        data = request.get_json()
        


        schema = GroupCreateschema()

        try:
            validated_data = schema.load(data)
        except ValidationError as err:
            return error_response(err.messages, 400)

        group, error = GroupService.create_group(
            validated_data["name"],
        )

        if error:
            return error_response(error, 500)

        return success_response(group.to_dict(), "Group created successfully", 201)

    
    @staticmethod
    def get_all_groups() -> Tuple:
        groups = GroupService.get_all_groups()
        groups_data = [group.to_dict() for group in groups]
        return success_response(groups_data, "groups retrieved successfully")
    
    @staticmethod
    def get_group_by_id(group_id: int) -> Tuple:
        group = GroupService.get_group_by_id(group_id)
        
        if not group:
            return error_response("group not found", 404)
        
        return success_response(group.to_dict(), "group retrieved successfully")
    
    @staticmethod
    def delete_group(group_id: int) -> Tuple:
        group = GroupService.get_group_by_id(group_id)
        
        if not group:
            return error_response("group not found", 404)
        
        success, error = GroupService.delete_group(group)
        
        if not success:
            return error_response(error, 500)
        
        return success_response(None, "group deleted successfully")