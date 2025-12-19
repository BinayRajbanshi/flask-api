from app import db
from datetime import datetime, timezone
from .user_groups import user_groups
from .group_permissions import group_permissions


class Group(db.Model):
    __tablename__ = "groups"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=True)
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc), nullable=True)

     # Relationship to User
    users = db.relationship(
        "User",
        secondary=user_groups,
        back_populates="groups"
    )

    # Relationship to permission
    permissions = db.relationship(
        "Permission",
        secondary=group_permissions,
        back_populates="groups"
    )

    def __repr__(self):
        return f"<Group {self.id}: {self.name}>"


# Converts a SQLAlchemy model instance into a plain Python dictionary.
# Useful for returning JSON responses in APIs.
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }