from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, NumberRange

class FeedbackForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired(message="This field is required.")])
    text = TextAreaField(label='Write your review here', validators=[DataRequired(message="This field is required.")])
    rating = IntegerField(label='Rate it from 1 to 5', validators=[DataRequired(message="This field is required."), NumberRange(min=1, max=5, message="Rating must be between 1 and 5.")])
    submit = SubmitField('Submit')