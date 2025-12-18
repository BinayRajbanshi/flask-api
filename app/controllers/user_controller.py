from flask import request
from typing import Tuple
from marshmallow import ValidationError

from app.services.user_service import UserService
from app.schemas.user_schems import UserCreateSchema
from app.utils.response import success_response, error_response

class UserController:
    @staticmethod
    def create_user() -> Tuple:
        data = request.get_json()
        
        if not data:
            return error_response("Request body is required", 400)

        schema = UserCreateSchema()

        try:
            validated_data = schema.load(data)
        except ValidationError as err:
            return error_response(err.messages, 400)

        user, error = UserService.create_user(
            validated_data["username"],
            validated_data["email"],
            validated_data["password"],
        )

        if error:
            return error_response(error, 500)

        return success_response(user.to_dict(), "User created successfully", 201)

    
    @staticmethod
    def get_all_users() -> Tuple:
        users = UserService.get_all_users()
        users_data = [user.to_dict() for user in users]
        return success_response(users_data, "users retrieved successfully")
    
    @staticmethod
    def get_user_by_id(user_id: int) -> Tuple:
        user = UserService.get_user_by_id(user_id)
        
        if not user:
            return error_response("user not found", 404)
        
        return success_response(user.to_dict(), "user retrieved successfully")
    
    # @staticmethod
    # def update_user(user_id: int) -> Tuple:
    #     user = userService.get_user_by_id(user_id)

    #     if not user:
    #         return error_response("user not found", 404)

    #     data = request.get_json()

    #     if not data:
    #         return error_response("Request body is required", 400)

    #     schema = userUpdateSchema()

    #     try:
    #         validated_data = schema.load(data)
    #     except ValidationError as err:
    #         return error_response(err.messages, 400)

    #     success, error = userService.update_user(
    #         user,
    #         validated_data.get("title"),
    #         validated_data.get("completed"),
    #     )

    #     if not success:
    #         return error_response(error, 500)

    #     from app import db
    #     db.session.refresh(user)

    #     return success_response(user.to_dict(), "user updated successfully")

    
    @staticmethod
    def delete_user(user_id: int) -> Tuple:
        user = UserService.get_user_by_id(user_id)
        
        if not user:
            return error_response("User not found", 404)
        
        success, error = UserService.delete_user(user)
        
        if not success:
            return error_response(error, 500)
        
        return success_response(None, "User deleted successfully")