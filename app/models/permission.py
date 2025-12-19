from app import db
from datetime import datetime, timezone
from .group_permissions import group_permissions


class Permission(db.Model):
    __tablename__ = "permissions"

    id = db.Column(db.Integer, primary_key=True)
    permission_code = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=True)
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc), nullable=True)

     # Relationship to Group
    groups = db.relationship(
        "Group",
        secondary=group_permissions,
        back_populates="permissions"
    )

    def __repr__(self):
        return f"<Permission {self.id}: {self.permission_code}>"


# Converts a SQLAlchemy model instance into a plain Python dictionary.
# Useful for returning JSON responses in APIs.
    def to_dict(self):
        return {
            "id": self.id,
            "permission_code": self.permission_code,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }