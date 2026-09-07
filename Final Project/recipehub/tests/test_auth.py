from flask_login import current_user

from app.models import User


def test_registration_creates_user(client, db):
    response = client.post(
        "/auth/register",
        data={
            "name": "New User",
            "email": "new@example.com",
            "password": "password123",
            "confirm_password": "password123",
        },
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert User.query.filter_by(email="new@example.com").first() is not None


def test_successful_login_authenticates_session(client, user):
    response = client.post(
        "/auth/login",
        data={"email": "alice@example.com", "password": "password123"},
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"Welcome back" in response.data
    assert current_user.is_authenticated
    assert current_user.email == "alice@example.com"


def test_failed_login_shows_error(client, user):
    response = client.post(
        "/auth/login",
        data={"email": "alice@example.com", "password": "wrong-password"},
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"Invalid email or password." in response.data


def test_logout(client, user, login):
    login("alice@example.com")
    response = client.get("/auth/logout", follow_redirects=True)
    assert b"You have been logged out." in response.data


def test_password_is_hashed(user):
    assert user.password_hash != "password123"
    assert user.check_password("password123")