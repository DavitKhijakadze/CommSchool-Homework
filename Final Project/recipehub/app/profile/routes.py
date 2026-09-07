import os
import secrets

from flask import (Blueprint, render_template, redirect, url_for, flash, abort, current_app)
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

from app.extensions import db
from app.models import User, Recipe
from app.profile.forms import ProfileForm

profile_bp = Blueprint("profile", __name__)


def save_profile_image(file_storage) -> str | None:
    """Validate the extension and store the image with a random, secure filename."""
    filename = secure_filename(file_storage.filename or "")
    if "." not in filename:
        return None
    extension = filename.rsplit(".", 1)[1].lower()
    if extension not in current_app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return None

    unique_name = f"{secrets.token_hex(12)}.{extension}"
    file_storage.save(os.path.join(current_app.config["UPLOAD_FOLDER"], unique_name))
    return unique_name


@profile_bp.route("/")
@login_required
def my_profile():
    recipes = (
        current_user.recipes.order_by(Recipe.created_at.desc()).all()
    )
    return render_template("profile/profile.html", user=current_user, recipes=recipes)


@profile_bp.route("/edit", methods=["GET", "POST"])
@login_required
def edit_profile():
    form = ProfileForm(obj=current_user)
    if form.validate_on_submit():
        current_user.name = form.name.data.strip()
        current_user.email = form.email.data.lower().strip()

        if form.profile_image.data:
            saved = save_profile_image(form.profile_image.data)
            if saved:
                current_user.profile_image = saved
            else:
                flash("Invalid image file. Profile picture was not changed.", "warning")

        db.session.commit()
        current_app.logger.info("Profile updated for user: %s", current_user.email)
        flash("Profile updated successfully.", "success")
        return redirect(url_for("profile.my_profile"))

    return render_template("profile/edit.html", form=form)


@profile_bp.route("/author/<int:user_id>")
def author(user_id):
    """Public author page - no sensitive data shown."""
    user = db.session.get(User, user_id)
    if user is None:
        abort(404)
    recipes = user.recipes.order_by(Recipe.created_at.desc()).all()
    return render_template("profile/author.html", user=user, recipes=recipes)