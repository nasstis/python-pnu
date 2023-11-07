from flask_wtf import FlaskForm
from wtforms import BooleanField, EmailField, IntegerField, StringField, PasswordField, SubmitField, TextAreaField, ValidationError
from wtforms.validators import DataRequired, Length, NumberRange, Email, EqualTo, Regexp

from app.models import User

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

class RegistrationForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired(message="This field is required."), 
                                                         Length(min=4, max=14, message='Username must be between 4 and 14 characters.'),
                                                         Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Username must have only letters, numbers, dots, or underscores')])
    email = EmailField('Email', validators=[DataRequired(message="This field is required."), Email(message="Invalid email.")])
    password =  PasswordField(label='Password', validators=[DataRequired(message="This field is required."), Length(min=6, message='Password must be more than 6 characters long')])
    confirm_password =  PasswordField(label='Confirm password', validators=[DataRequired(message="This field is required."), EqualTo('password', message='Passwords must match.')])
    submit = SubmitField('Sign up')

    def validate_username(self, field):
        user = User.query.filter_by(username=field.data).first()
        if user:
            raise ValidationError('Username already exists. Choose a different one.')

    def validate_email(self, field):
        user = User.query.filter_by(email=field.data).first()
        if user:
            raise ValidationError('Email already exists. Please use a different one.')

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(message="This field is required."), Email(message="Invalid email.")])
    password = PasswordField(label='Password', validators=[DataRequired(message="This field is required."), Length(min=6, message='Password must be more than 6 characters long')])
    remember = BooleanField(label='Remember me')
    submit = SubmitField("Login")
