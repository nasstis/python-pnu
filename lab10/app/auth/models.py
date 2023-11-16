import datetime
from flask_login import UserMixin
from app import db, bcrypt, login_manager


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password_hash = db.Column(db.String(128))
    last_seen = db.Column(db.DateTime, default=datetime.datetime.now)
    about_me = db.Column(db.String(240))

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    
    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, pwd):
        return bcrypt.check_password_hash(self.password_hash, pwd)