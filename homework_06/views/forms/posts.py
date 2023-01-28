from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    title = StringField(
        label="Title",
        name="title",
        validators=[
            DataRequired(),
            Length(min=3, max=30),
        ],
    )
    body = TextAreaField(validators=[DataRequired()])
    user = SelectField('Username', coerce=int)