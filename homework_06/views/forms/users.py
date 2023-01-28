from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length, Email


class UserForm(FlaskForm):
    username = StringField(
        label="Username",
        name="user-name",
        validators=[
            DataRequired(),
            Length(min=3, max=30),
        ],
    )
    email = StringField(
        label="Email",
        name="user-email",
        validators=[
            DataRequired(),
            Email(),
            Length(min=3, max=30),
        ],
    )
