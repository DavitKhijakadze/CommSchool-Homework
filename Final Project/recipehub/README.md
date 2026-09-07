README.md


# RecipeHub – Recipe Sharing and Search Web Portal

RecipeHub is a Flask web application where users register, publish their own recipes,
browse and search recipes from the community, and view live nutrition information
fetched from the Spoonacular API.

## Features

- User registration with validation and hashed passwords (Werkzeug)
- Login / logout with Flask-Login sessions
- Anonymous users can browse recipes, view details and read the About page
- Authenticated users can add, edit and delete **their own** recipes (server-side ownership checks)
- Card-based recipe list, newest first, with clickable author links
- Server-side search by title/description and filter by category
- 11 predefined categories
- Recipe detail page with a dynamic nutrition section (Spoonacular API)
- User profile with image upload, name and email editing
- Public author pages
- CSRF protection on every form (Flask-WTF + CSRFProtect)
- Custom 403 / 404 / 500 error pages
- Rotating file logging to `logs/app.log`
- pytest test suite (routes, authentication, authorization)
- Bootstrap 5 responsive UI
- Ready for deployment on Render with Gunicorn

## Technology stack

Python 3.11+, Flask, Jinja2, Flask-WTF/WTForms, Flask-SQLAlchemy, Flask-Login,
Flask-Migrate (Alembic), Werkzeug, SQLite (dev) / PostgreSQL (prod), requests,
python-dotenv, pytest, Gunicorn, Bootstrap 5, Font Awesome.

## Project structure

- `app/` – application package (application factory in `__init__.py`)
- `app/models.py` – `User` and `Recipe` SQLAlchemy models
- `app/auth/`, `app/recipes/`, `app/profile/`, `app/main/` – blueprints (routes + forms)
- `app/services/spoonacular_service.py` – external API integration
- `app/templates/`, `app/static/` – Jinja2 templates and assets
- `tests/` – pytest suite and fixtures
- `config.py` – Development / Testing / Production configuration
- `run.py` – entry point (`gunicorn run:app`)
- `seed.py` – optional demo data

## Installation

```bash
python -m venv venv

# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate

pip install -r requirements.txt
```

## Environment variables

Copy `.env.example` to `.env` and fill in the values:

```text
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///recipehub.db
SPOONACULAR_API_KEY=your-spoonacular-api-key
FLASK_CONFIG=development
```

`.env` is git-ignored and must never be committed.
If `DATABASE_URL` is missing, SQLite is used automatically in development.

## Database setup

```bash
flask --app run.py db init
flask --app run.py db migrate -m "Initial migration"
flask --app run.py db upgrade
```

Optional demo data (2–3 users, several recipes):

```bash
python seed.py
```

## Run locally

```bash
python run.py
```

or

```bash
flask --app run.py run --debug
```

Open http://127.0.0.1:5000

## Testing

```bash
pytest
```

Tests use an isolated in-memory SQLite database, so your local data is never touched.

## Logging

Logs are written to `logs/app.log` (rotating, 1 MB × 3 backups) and to the console.
Logged events: successful login, failed login, registration, recipe create/edit/delete,
unauthorized actions, Spoonacular API errors and server exceptions.
Passwords and API keys are never logged.

## External API

1. Create a free account at https://spoonacular.com/food-api
2. Copy your API key into `SPOONACULAR_API_KEY` in `.env`
3. The nutrition block appears on the recipe detail page.
   If the key is missing or the API fails, the page shows
   "Nutrition information is currently unavailable." and the error is logged.

## Deployment (Render)

1. Push the project to GitHub.
2. On Render, create a **PostgreSQL** database and copy its Internal Database URL.
3. Create a **Web Service** from the repository:
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `gunicorn run:app`
4. Add environment variables: `SECRET_KEY`, `DATABASE_URL`, `SPOONACULAR_API_KEY`,
   `FLASK_CONFIG=production`, `PYTHON_VERSION=3.11.9`
5. Run migrations once from the Render Shell:
   ```bash
   flask --app run.py db upgrade
   ```

`config.py` automatically converts `postgres://` URLs to `postgresql://`.

## Upload to GitHub

```bash
git init
git add .
git commit -m "Initial RecipeHub project"
git branch -M main
git remote add origin YOUR_REPOSITORY_URL
git push -u origin main
```