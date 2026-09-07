import os
from app import create_app
from app.extensions import db
from app.models import User, Recipe

app = create_app(os.environ.get("FLASK_CONFIG", "development"))


@app.shell_context_processor
def shell_context():
    return {"db": db, "User": User, "Recipe": Recipe}


if __name__ == "__main__":
    app.run(debug=app.config.get("DEBUG", False))