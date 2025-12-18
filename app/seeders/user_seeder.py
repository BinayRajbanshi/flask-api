# app/seeds/users.py
from app import db
from app.models.user import User

def seed_users():
    users = [
        User(username="jane", email="jane@example.com",password_hash="this is hashed password_hash"),
        User(username="john", email="john@example.com", password_hash="this is another hashed password_hash"),
        User(username="binay", email="binay@gmail.com", password_hash="this hashed"),
        User(username="ankit", email="ankit@gmail.com", password_hash="hashed again")
    ]

    db.session.add_all(users)
    db.session.commit()
