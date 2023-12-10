from flask import redirect, render_template, url_for, flash
from .forms import FeedbackForm
from .models import Feedback
from app.auth.models import User
from . import users_blueprint
from app import db

@users_blueprint.route('/review', methods=['GET', 'POST'])
def review():
    form = FeedbackForm()

    if form.validate_on_submit():
        name = form.name.data
        text = form.text.data
        rating = form.rating.data
        feedback = Feedback(name=name, text=text, rating=rating)
        try:
            db.session.add(feedback)
            db.session.commit()
            flash('Your review added successfully', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'An error occurred: {str(e)}', 'danger')
        return redirect(url_for("users.review"))

    reviews = Feedback.query.all()
    return render_template("review.html", form=form, reviews=reviews)

@users_blueprint.route('/users')
def users():
    users = User.query.all()
    total_users = len(users)
    return render_template('users.html', users=users, total_users=total_users)