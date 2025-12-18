from flask import request
from typing import Tuple
from marshmallow import ValidationError

from app.services.todo_service import TodoService
from app.schemas.todo_schema import TodoCreateSchema, TodoUpdateSchema
from app.utils.response import success_response, error_response



class TodoController:
    @staticmethod
    def create_todo() -> Tuple:
        data = request.get_json()



        schema = TodoCreateSchema()

        try:
            validated_data = schema.load(data)
        except ValidationError as err:
            return error_response(err.messages, 400)

        todo, error = TodoService.create_todo(
            validated_data["title"],
            validated_data["completed"],
        )

        if error:
            return error_response(error, 500)

        return success_response(todo.to_dict(), "Todo created successfully", 201)

    
    @staticmethod
    def get_all_todos() -> Tuple:
        todos = TodoService.get_all_todos()
        todos_data = [todo.to_dict() for todo in todos]
        return success_response(todos_data, "Todos retrieved successfully")
    
    @staticmethod
    def get_todo(todo_id: int) -> Tuple:
        todo = TodoService.get_todo_by_id(todo_id)
        
        if not todo:
            return error_response("Todo not found", 404)
        
        return success_response(todo.to_dict(), "Todo retrieved successfully")
    
    @staticmethod
    def update_todo(todo_id: int) -> Tuple:
        todo = TodoService.get_todo_by_id(todo_id)

        if not todo:
            return error_response("Todo not found", 404)

        data = request.get_json()



        schema = TodoUpdateSchema()

        try:
            validated_data = schema.load(data)
        except ValidationError as err:
            return error_response(err.messages, 400)

        success, error = TodoService.update_todo(
            todo,
            validated_data.get("title"),
            validated_data.get("completed"),
        )

        if not success:
            return error_response(error, 500)

        from app import db
        db.session.refresh(todo)

        return success_response(todo.to_dict(), "Todo updated successfully")

    
    @staticmethod
    def delete_todo(todo_id: int) -> Tuple:
        todo = TodoService.get_todo_by_id(todo_id)
        
        if not todo:
            return error_response("Todo not found", 404)
        
        success, error = TodoService.delete_todo(todo_id)
        
        if not success:
            return error_response(error, 500)
        
        return success_response(None, "Todo deleted successfully")

