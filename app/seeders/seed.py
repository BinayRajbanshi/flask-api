# app/seeders/seed.py
from app import create_app, db
from app.seeders.user_seeder import seed_users
from app.seeders.permission_seeder import seed_permissions

def run():
    app = create_app()
    with app.app_context():
        # seed_users()
        seed_permissions()
        print("Seeding completed")

if __name__ == "__main__":
    run()
