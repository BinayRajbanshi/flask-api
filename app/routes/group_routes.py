from flask import Blueprint
from app.controllers.group_controller import GroupController

group_bp = Blueprint("group", __name__, url_prefix="/api/v1/groups")

# Initialize controller
controller = GroupController()

# Route definitions
@group_bp.route("", methods=["POST"])
def create_group():
    return controller.create_group()

@group_bp.route("", methods=["GET"])
def get_groups():
    return controller.get_all_groups()

@group_bp.route("/<int:group_id>", methods=["GET"])
def get_group(group_id):
    return controller.get_group_by_id(group_id)

@group_bp.route("/<int:group_id>", methods=["DELETE"])
def delete_group(group_id):
    return controller.delete_group(group_id)