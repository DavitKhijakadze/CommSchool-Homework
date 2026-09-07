from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_user, logout_user, login_required, current_user

from app.extensions import db
from app.models import User
from app.auth.forms import RegistrationForm, LoginForm

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(name=form.name.data.strip(), email=form.email.data.lower().strip())
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        current_app.logger.info("New user registered: %s", user.email)
        flash("Registration successful. You can log in now.", "success")
        return redirect(url_for("auth.login"))

    return render_template("auth/register.html", form=form)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data.lower().strip()
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            current_app.logger.info("Successful login for user: %s", email)
            flash(f"Welcome back, {user.name}!", "success")
            next_page = request.args.get("next")
            # Only allow relative redirects (open-redirect protection).
            if not next_page or not next_page.startswith("/"):
                next_page = url_for("main.index")
            return redirect(next_page)

        current_app.logger.warning("Failed login attempt for email: %s", email)
        flash("Invalid email or password.", "danger")

    return render_template("auth/login.html", form=form)


@auth_bp.route("/logout")
@login_required
def logout():
    current_app.logger.info("User logged out: %s", current_user.email)
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("main.index"))