from flask import (Blueprint, render_template, redirect, url_for, flash, abort, current_app)
from flask_login import login_required, current_user

from app.extensions import db
from app.models import Recipe
from app.recipes.forms import RecipeForm, DeleteRecipeForm
from app.services.spoonacular_service import get_recipe_nutrition

recipes_bp = Blueprint("recipes", __name__)


def get_owned_recipe_or_403(recipe_id: int) -> Recipe:
    """Load a recipe and make sure the current user owns it."""
    recipe = db.session.get(Recipe, recipe_id)
    if recipe is None:
        abort(404)
    if recipe.author_id != current_user.id:
        current_app.logger.warning(
            "Unauthorized action on recipe %s by user: %s", recipe.id, current_user.email
        )
        abort(403)
    return recipe


@recipes_bp.route("/<int:recipe_id>")
def detail(recipe_id):
    recipe = db.session.get(Recipe, recipe_id)
    if recipe is None:
        abort(404)
    nutrition = get_recipe_nutrition(recipe)
    delete_form = DeleteRecipeForm()
    return render_template(
        "recipes/detail.html", recipe=recipe, nutrition=nutrition, delete_form=delete_form
    )


@recipes_bp.route("/add", methods=["GET", "POST"])
@login_required
def add_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        recipe = Recipe(
            title=form.title.data.strip(),
            short_description=form.short_description.data.strip(),
            instructions=form.instructions.data.strip(),
            category=form.category.data,
            preparation_time=form.preparation_time.data,
            servings=form.servings.data,
            author=current_user,  # author never comes from the client
        )
        db.session.add(recipe)
        db.session.commit()
        current_app.logger.info("Recipe created: %s by %s", recipe.title, current_user.name)
        flash("Recipe added successfully.", "success")
        return redirect(url_for("recipes.detail", recipe_id=recipe.id))

    return render_template("recipes/add.html", form=form)


@recipes_bp.route("/<int:recipe_id>/edit", methods=["GET", "POST"])
@login_required
def edit_recipe(recipe_id):
    recipe = get_owned_recipe_or_403(recipe_id)
    form = RecipeForm(obj=recipe)
    if form.validate_on_submit():
        recipe.title = form.title.data.strip()
        recipe.short_description = form.short_description.data.strip()
        recipe.instructions = form.instructions.data.strip()
        recipe.category = form.category.data
        recipe.preparation_time = form.preparation_time.data
        recipe.servings = form.servings.data
        db.session.commit()
        current_app.logger.info("Recipe edited: %s by %s", recipe.title, current_user.name)
        flash("Recipe updated successfully.", "success")
        return redirect(url_for("recipes.detail", recipe_id=recipe.id))

    return render_template("recipes/edit.html", form=form, recipe=recipe)


@recipes_bp.route("/<int:recipe_id>/delete", methods=["POST"])
@login_required
def delete_recipe(recipe_id):
    recipe = get_owned_recipe_or_403(recipe_id)
    form = DeleteRecipeForm()
    if not form.validate_on_submit():
        abort(400)

    title = recipe.title
    db.session.delete(recipe)
    db.session.commit()
    current_app.logger.info("Recipe deleted: %s by %s", title, current_user.name)
    flash("Recipe deleted.", "success")
    return redirect(url_for("main.index"))