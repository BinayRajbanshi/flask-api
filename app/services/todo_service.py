from typing import List, Optional
from app import db
from app.models.todo import Todo
from sqlalchemy.exc import SQLAlchemyError


class TodoService:
    @staticmethod
    def create_todo(title: str, completed: bool = False) -> tuple[Optional[Todo], Optional[str]]:
        try:
            todo = Todo(title=title, completed=completed)
            db.session.add(todo)
            db.session.commit()
            return todo, None
        except SQLAlchemyError as e:
            db.session.rollback()
            return None, f"Database error: {str(e)}"
        except Exception as e:
            db.session.rollback()
            return None, f"Unexpected error: {str(e)}"
    
    @staticmethod
    def get_all_todos() -> List[Todo]:
        try:
            return Todo.query.order_by(Todo.created_at.desc()).all()
        except SQLAlchemyError:
            return []
    
    @staticmethod
    def get_todo_by_id(todo_id: int) -> Optional[Todo]:
        try:
            return Todo.query.get(todo_id)
        except SQLAlchemyError:
            return None
    
    @staticmethod
    def update_todo(todo: Todo, title: Optional[str] = None, completed: Optional[bool] = None) -> tuple[bool, Optional[str]]:
        try:
            if title is not None:
                todo.title = title
            if completed is not None:
                todo.completed = completed
            
            db.session.commit()
            return True, None
        except SQLAlchemyError as e:
            db.session.rollback()
            return False, f"Database error: {str(e)}"
        except Exception as e:
            db.session.rollback()
            return False, f"Unexpected error: {str(e)}"
    
    @staticmethod
    def delete_todo(todo: Todo) -> tuple[bool, Optional[str]]:
        try:
            db.session.delete(todo)
            db.session.commit()
            return True, None
        except SQLAlchemyError as e:
            db.session.rollback()
            return False, f"Database error: {str(e)}"
        except Exception as e:
            db.session.rollback()
            return False, f"Unexpected error: {str(e)}"

