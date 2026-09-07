import os
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))


def normalize_db_url(url: str) -> str:
    """Render/Heroku give 'postgres://' but SQLAlchemy needs 'postgresql://'."""
    if url and url.startswith("postgres://"):
        url = url.replace("postgres://", "postgresql://", 1)
    return url


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-change-me")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SPOONACULAR_API_KEY = os.environ.get("SPOONACULAR_API_KEY")
    SPOONACULAR_TIMEOUT = 5  # seconds
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "app", "static", "uploads")
    ALLOWED_IMAGE_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "webp"}
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024  # 2 MB uploads
    LOG_DIR = os.path.join(BASE_DIR, "logs")


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = normalize_db_url(
        os.environ.get("DATABASE_URL") or "sqlite:///" + os.path.join(BASE_DIR, "recipehub.db")
    )


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False  # disabled so tests can post forms easily
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SECRET_KEY = "testing-secret"


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = normalize_db_url(
        os.environ.get("DATABASE_URL") or "sqlite:///" + os.path.join(BASE_DIR, "recipehub.db")
    )


config_by_name = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}