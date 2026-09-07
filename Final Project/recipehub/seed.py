import os

from app import create_app
from app.extensions import db
from app.models import User, Recipe

config_name = os.environ.get("FLASK_CONFIG", "development")
if config_name == "production":
    raise SystemExit("Refusing to seed demo data in production.")

app = create_app(config_name)

USERS = [
    ("John Doe", "john@example.com", "password123"),
    ("Maria Rossi", "maria@example.com", "password123"),
    ("Nino Beridze", "nino@example.com", "password123"),
]

RECIPES = [
    ("Pasta Carbonara", "Classic Roman pasta with eggs, pecorino and pancetta.",
     "1. Boil the pasta.\n2. Fry pancetta.\n3. Mix eggs with cheese.\n4. Combine off the heat.",
     "Dinner", 25, 2, 0),
    ("Avocado Toast", "Quick and healthy breakfast in five minutes.",
     "1. Toast the bread.\n2. Mash avocado with lemon and salt.\n3. Spread and serve.",
     "Breakfast", 10, 1, 0),
    ("Vegan Lentil Soup", "Warming lentil soup with carrots and celery.",
     "1. Sauté vegetables.\n2. Add lentils and stock.\n3. Simmer 30 minutes.",
     "Soup", 40, 4, 1),
    ("Greek Salad", "Fresh tomatoes, cucumber, olives and feta.",
     "1. Chop vegetables.\n2. Add olives and feta.\n3. Dress with olive oil and oregano.",
     "Salad", 15, 2, 1),
    ("Chocolate Brownies", "Fudgy brownies with a crackly top.",
     "1. Melt chocolate and butter.\n2. Whisk in sugar and eggs.\n3. Fold in flour.\n4. Bake 25 min.",
     "Dessert", 45, 8, 2),
    ("Khachapuri", "Georgian cheese-filled bread.",
     "1. Prepare dough.\n2. Fill with cheese.\n3. Bake until golden.",
     "Main Course", 90, 4, 2),
]

with app.app_context():
    db.create_all()
    users = []
    for name, email, password in USERS:
        user = User.query.filter_by(email=email).first()
        if user is None:
            user = User(name=name, email=email)
            user.set_password(password)
            db.session.add(user)
        users.append(user)
    db.session.commit()

    for title, desc, steps, category, prep, servings, author_index in RECIPES:
        if Recipe.query.filter_by(title=title).first():
            continue
        db.session.add(Recipe(
            title=title, short_description=desc, instructions=steps,
            category=category, preparation_time=prep, servings=servings,
            author=users[author_index],
        ))
    db.session.commit()
    print("Seed data created. Demo login: john@example.com / password123")