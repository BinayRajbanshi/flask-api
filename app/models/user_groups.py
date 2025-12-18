from datetime import datetime, timezone
from app import db

user_groups = db.Table(
    "user_groups",
    db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
    db.Column("group_id", db.Integer, db.ForeignKey("groups.id"), primary_key=True),
    db.Column("created_at", db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
)
