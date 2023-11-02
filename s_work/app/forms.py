from flask_wtf import FlaskForm
from wtforms import BooleanField, IntegerField, StringField, PasswordField, SubmitField, TextAreaField, ValidationError
from wtforms.validators import DataRequired, Length, NumberRange

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

class TodoForm(FlaskForm):
    title = StringField("Enter a task here", validators=[DataRequired(message="This field is required.")])
    description = StringField("Describe your task", validators=[DataRequired(message="This field is required.")])
    submit = SubmitField("Save")

class FeedbackForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired(message="This field is required.")])
    text = TextAreaField(label='Write your review here', validators=[DataRequired(message="This field is required.")])
    rating = IntegerField(label='Rate it from 1 to 5', validators=[DataRequired(message="This field is required."), NumberRange(min=1, max=5, message="Rating must be between 1 and 5.")])
    submit = SubmitField('Submit')
