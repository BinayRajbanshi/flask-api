"""
Idempotent Permission Seeder
"""

# from app import create_app, db
# from app.models.permission import Permission 

from app import db
from app.models.permission import Permission


PERMISSIONS = [
    # Todo permissions
    {
        "permission_code": "todo:create",
    },
    {
        "permission_code": "todo:read",
    },
    {
        "permission_code": "todo:update",
    },
    {
        "permission_code": "todo:delete",
    },

    # User permissions
    {
        "permission_code": "user:create",
    },
    {
        "permission_code": "user:read",
    },
    {
        "permission_code": "user:update",
    },
    {
        "permission_code": "user:delete",
    },
]


def seed_permissions():
    created = 0
    skipped = 0

    for perm in PERMISSIONS:
        existing = Permission.query.filter_by(permission_code=perm["permission_code"]).first()

        if existing:
            skipped += 1
            continue

        permission = Permission(
            permission_code=perm["permission_code"],
        )

        db.session.add(permission)
        created += 1

    db.session.commit()

    print("Permission seeding completed")
    print(f"Created: {created}")
    print(f"Skipped (already existed): {skipped}")
