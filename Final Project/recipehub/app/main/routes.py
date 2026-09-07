from flask import Blueprint, render_template, request

from app.models import Recipe, User, CATEGORIES

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    """Recipes list, newest first, with server-side search and category filter."""
    query_text = request.args.get("q", "", type=str).strip()
    category = request.args.get("category", "", type=str).strip()

    query = Recipe.query.join(User)

    if query_text:
        like = f"%{query_text}%"
        query = query.filter(
            Recipe.title.ilike(like) | Recipe.short_description.ilike(like)
        )
    if category and category in CATEGORIES:
        query = query.filter(Recipe.category == category)

    recipes = query.order_by(Recipe.created_at.desc()).all()
    return render_template(
        "recipes/index.html", recipes=recipes, q=query_text, selected_category=category
    )


@main_bp.route("/about")
def about():
    return render_template("main/about.html")