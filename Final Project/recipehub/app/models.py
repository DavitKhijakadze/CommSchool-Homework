from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app.extensions import db, login_manager

# Predefined recipe categories used by the forms and the search filter.
CATEGORIES = [
    "Breakfast", "Lunch", "Dinner", "Dessert", "Vegan", "Vegetarian",
    "Main Course", "Salad", "Soup", "Snack", "Other",
]


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    profile_image = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    recipes = db.relationship(
        "Recipe", back_populates="author", cascade="all, delete-orphan", lazy="dynamic"
    )

    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    @property
    def avatar_url(self) -> str:
        """Uploaded picture or the default avatar."""
        from flask import url_for
        if self.profile_image:
            return url_for("static", filename=f"uploads/{self.profile_image}")
        return url_for("static", filename="img/default-avatar.png")

    def __repr__(self):
        return f"<User {self.email}>"


class Recipe(db.Model):
    __tablename__ = "recipes"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False, index=True)
    short_description = db.Column(db.String(300), nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False, index=True)
    preparation_time = db.Column(db.Integer, nullable=False)  # minutes
    servings = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)

    author = db.relationship("User", back_populates="recipes")

    def is_owned_by(self, user) -> bool:
        return user.is_authenticated and self.author_id == user.id

    def __repr__(self):
        return f"<Recipe {self.title}>"


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))