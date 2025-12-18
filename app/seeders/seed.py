# app/seeders/seed.py
from app import create_app, db
from app.seeders.user_seeder import seed_users

def run():
    app = create_app()
    with app.app_context():
        seed_users()
        print("Seeding completed")

if __name__ == "__main__":
    run()
