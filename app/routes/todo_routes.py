from flask import Blueprint
from app.controllers.todo_controller import TodoController

todo_bp = Blueprint("todo", __name__, url_prefix="/api/v1/todos")

# Initialize controller
todo_controller = TodoController()

# Route definitions
@todo_bp.route("", methods=["POST"])
def create_todo():
    return todo_controller.create_todo()

@todo_bp.route("", methods=["GET"])
def get_todos():
    return todo_controller.get_all_todos()

@todo_bp.route("/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    return todo_controller.get_todo(todo_id)

@todo_bp.route("/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    return todo_controller.update_todo(todo_id)

@todo_bp.route("/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    return todo_controller.delete_todo(todo_id)

