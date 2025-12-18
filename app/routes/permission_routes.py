from flask import Blueprint
from app.controllers.permission_controller import PermissionController

permission_bp = Blueprint("permission", __name__, url_prefix="/api/v1/permissions")

# Initialize controller
controller = PermissionController()


@permission_bp.route("", methods=["GET"])
def get_permissions():
    return controller.get_all_permissions()

@permission_bp.route("/<int:permission_id>", methods=["GET"])
def get_permission(permission_id):
    return controller.get_permission_by_id(permission_id)