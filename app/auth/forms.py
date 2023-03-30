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
    password = PasswordField(
                             "Password",
                             validators=[validators.DataRequired(message="Password is required"),
                                         validators.Length(min=6, message="Min 6 length of password is required")]
                             )
    remember = BooleanField("Remember")
    submit = SubmitField("Log In")


class RegisterForm(LoginForm):
    email = StringField("Email", validators=[validators.DataRequired(message="Email is required"), validators.Email()])
    confirm_password = PasswordField(
                             "Confirm Password",
                             validators=[validators.DataRequired(message="Confirm Password is required"),
                                         validators.EqualTo("password", message="Passwords must match")]
                             )
    submit = SubmitField("Register")
