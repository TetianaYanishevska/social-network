from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    SubmitField,
    validators
    )


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[validators.DataRequired(message="Username is required")])
    password = PasswordField("Password",
                             validators=[validators.DataRequired(message="Password is required"),
                             validators.Length(min=6, message="Min 6 length of password is required")]
                             )
    remember = BooleanField("Remember")
    submit = SubmitField("Log In")


class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[validators.DataRequired(message="Username is required")])
    email = StringField("Email", validators=[validators.DataRequired(message="Email is required"), validators.Email()])
    password = PasswordField("Password",
                             validators=[validators.DataRequired(message="Password is required"),
                                         validators.Length(min=6, message="Min 6 length of password is required")]
                             )
    submit = SubmitField("Log In")
