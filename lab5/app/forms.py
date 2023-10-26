from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired(message="This field is required.")])
    password = PasswordField(label='Password', validators=[DataRequired(message="This field is required."), Length(min=4, max=10, message='The password must be between 4 and 10 characters.')])
    remember = BooleanField(label='Remember me')
    submit = SubmitField("Sign In")

class ChangePasswordForm(FlaskForm):
    current_password = PasswordField(label='Current Password', validators=[DataRequired(message="This field is required."), Length(min=4, max=10, message='The password must be between 4 and 10 characters.')])
    new_password = PasswordField(label='New Password', validators=[DataRequired(message="This field is required."), Length(min=4, max=10, message='The password must be between 4 and 10 characters.')])
    confirm_password = PasswordField(label='Confirm New Password', validators=[DataRequired(message="This field is required."), Length(min=4, max=10, message='The password must be between 4 and 10 characters.')])
    submit = SubmitField("Change Password")