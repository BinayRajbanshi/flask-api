from flask import jsonify
from typing import Any, Dict, Optional


def success_response(data: Any = None, message: str = "Success", status_code: int = 200) -> tuple:
    response: Dict[str, Any] = {
        "success": True,
        "message": message
    }
    
    if data is not None:
        response["data"] = data
    
    return jsonify(response), status_code


def error_response(message: str = "An error occurred", status_code: int = 400, errors: Optional[Dict] = None) -> tuple:
    response: Dict[str, Any] = {
        "success": False,
        "message": message
    }
    
    if errors:
        response["errors"] = errors
    
    return jsonify(response), status_code

