from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length, ValidationError
from flask_login import current_user

from app.models import User


class ProfileForm(FlaskForm):
    name = StringField("Full name", validators=[DataRequired(), Length(2, 120)])
    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=120)])
    profile_image = FileField(
        "Profile image",
        validators=[FileAllowed(["png", "jpg", "jpeg", "gif", "webp"], "Images only!")],
    )
    submit = SubmitField("Save changes")

    def validate_email(self, field):
        email = field.data.lower().strip()
        existing = User.query.filter_by(email=email).first()
        if existing and existing.id != current_user.id:
            raise ValidationError("This email is already in use.")