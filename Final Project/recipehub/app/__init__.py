import os
from flask import Flask

from app.extensions import db, login_manager, migrate, csrf
from app.logging_config import configure_logging
from app.errors import register_error_handlers
from config import config_by_name

def create_app(config_name: str = "development") -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_by_name.get(config_name, config_by_name["development"]))

    # Extensions
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    configure_logging(app)
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

    # Blueprints
    from app.main.routes import main_bp
    from app.auth.routes import auth_bp
    from app.recipes.routes import recipes_bp
    from app.profile.routes import profile_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(recipes_bp, url_prefix="/recipes")
    app.register_blueprint(profile_bp, url_prefix="/profile")

    register_error_handlers(app)

    # Make categories available in every template (search dropdown).
    from app.models import CATEGORIES

    @app.context_processor
    def inject_globals():
        return {"categories": CATEGORIES}

    return app