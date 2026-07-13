import pytest


def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def test_celsius_to_fahrenheit_zero():
    assert pytest.approx(celsius_to_fahrenheit(0)) == 32

def test_celsius_to_fahrenheit_100():
    assert pytest.approx(celsius_to_fahrenheit(100)) == 212

def test_celsius_to_fahrenheit_negative():
    assert pytest.approx(celsius_to_fahrenheit(-40)) == -40


users = {
    "davit": "1234",
    "nino": "qwerty"
}


def check_login(username, password):
    if username not in users:
        raise ValueError("User not found")
    if users[username] != password:
        raise ValueError("Incorrect password")
    return True


def test_check_login_correct():
    assert check_login("davit", "1234") is True

def test_check_login_wrong_password():
    with pytest.raises(ValueError):
        check_login("davit", "wrongpass")

def test_check_login_user_not_found():
    with pytest.raises(ValueError):
        check_login("giorgi", "1234")


def is_valid_email(email):
    return "@" in email and "." in email


@pytest.mark.parametrize("email, expected", [
    ("test@gmail.com", True),
    ("davit.khijakadze@mail.com", True),
    ("wrongemail.com", False),
    ("wrong@email", False),
    ("", False)
])
def test_is_valid_email(email, expected):
    assert is_valid_email(email) == expected
