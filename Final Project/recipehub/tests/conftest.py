import pytest

from app import create_app
from app.extensions import db as _db
from app.models import User, Recipe


@pytest.fixture
def app():
    app = create_app("testing")
    with app.app_context():
        _db.create_all()
        yield app
        _db.session.remove()
        _db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def db(app):
    return _db


def create_user(name, email, password="password123"):
    user = User(name=name, email=email)
    user.set_password(password)
    _db.session.add(user)
    _db.session.commit()
    return user


@pytest.fixture
def user(db):
    """User A – the recipe owner."""
    return create_user("Alice Owner", "alice@example.com")


@pytest.fixture
def other_user(db):
    """User B – the attacker."""
    return create_user("Bob Stranger", "bob@example.com")


@pytest.fixture
def recipe(db, user):
    recipe = Recipe(
        title="Pasta Carbonara",
        short_description="Classic Roman pasta with eggs and pancetta.",
        instructions="Boil pasta. Fry pancetta. Mix with eggs and cheese.",
        category="Dinner",
        preparation_time=25,
        servings=2,
        author=user,
    )
    _db.session.add(recipe)
    _db.session.commit()
    return recipe


@pytest.fixture
def login(client):
    """Helper that logs a user in via the real login form."""
    def _login(email, password="password123"):
        return client.post(
            "/auth/login",
            data={"email": email, "password": password},
            follow_redirects=True,
        )
    return _login