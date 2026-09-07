from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

from app.models import CATEGORIES


class RecipeForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(3, 150)])
    short_description = TextAreaField(
        "Short description", validators=[DataRequired(), Length(10, 300)]
    )
    instructions = TextAreaField("Full recipe / instructions", validators=[DataRequired()])
    category = SelectField(
        "Category", choices=[(c, c) for c in CATEGORIES], validators=[DataRequired()]
    )
    preparation_time = IntegerField(
        "Preparation time (minutes)",
        validators=[DataRequired(), NumberRange(min=1, max=1440, message="Must be a positive number.")],
    )
    servings = IntegerField(
        "Servings",
        validators=[DataRequired(), NumberRange(min=1, max=100, message="Must be a positive number.")],
    )
    submit = SubmitField("Save recipe")


class DeleteRecipeForm(FlaskForm):
    """Empty form used only to provide a CSRF token for the delete POST."""
    submit = SubmitField("Delete")