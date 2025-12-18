from datetime import datetime, timezone
from app import db

group_permissions = db.Table(
    "group_permissions",
    db.Column("group_id", db.Integer, db.ForeignKey("groups.id"), primary_key=True),
    db.Column("permission_id", db.Integer, db.ForeignKey("permissions.id"), primary_key=True),
    db.Column("created_at", db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
)