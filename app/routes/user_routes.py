from flask import Blueprint
from app.controllers.user_controller import UserController

user_bp = Blueprint("user", __name__, url_prefix="/api/v1/users")

# Initialize controller
controller = UserController()

# Route definitions
@user_bp.route("", methods=["POST"])
def create_user():
    return controller.create_user()

@user_bp.route("", methods=["GET"])
def get_todos():
    return controller.get_all_users()

@user_bp.route("/<int:user_id>", methods=["GET"])
def get_todo(user_id):
    return controller.get_user_by_id(user_id)

# @user_bp.route("/<int:todo_id>", methods=["PUT"])
# def update_todo(todo_id):
#     return todo_controller.update_todo(todo_id)

@user_bp.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    return controller.delete_user(user_id)