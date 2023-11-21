from datetime import datetime
from app import db


class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    text = db.Column(db.String)
    image = db.Column(db.String, default='postdefault.jpg')
    created = db.Column(db.TIMESTAMP, default=datetime.now)
    type = db.Column(db.Enum('news', 'publication', 'other'), default='news')
    enabled = db.Column(db.Boolean, default=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"<Post {self.id}: {self.title}>"