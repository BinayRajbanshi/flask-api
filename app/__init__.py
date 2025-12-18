"""Flask application factory."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import config

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name: str = None):
    """        
    Returns:
        Flask application instance
    """
    app = Flask(__name__)
    
    # Load configuration
    config_name = config_name or "default"
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Register blueprints
    from app.routes import todo_bp, user_bp, group_bp, permission_bp
    app.register_blueprint(todo_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(group_bp)
    app.register_blueprint(permission_bp)
    
    
    
    return app