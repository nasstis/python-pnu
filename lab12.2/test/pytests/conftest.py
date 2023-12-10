import pytest
from app import create_app, db

from flask import url_for
from app.auth.models import User

from app.post.models import Category, Post, Tag


@pytest.fixture(scope='module')
def client():
    app = create_app('test')
    app.config['SERVER_NAME'] = '127.0.0.1:5000'

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()

@pytest.fixture(scope='module')
def new_user():
    user = User(username='Test User', email='test.user@gmail.com', password='password')
    yield user
    
@pytest.fixture(scope='module')
def categories():
    categories = [
        Category(name='Sport'),
        Category(name='Art')
    ]
    yield categories

@pytest.fixture(scope='module')
def tags():
    tags = [
        Tag(name='cats'),
        Tag(name='music')
    ]
    yield tags
    
@pytest.fixture(scope='module')
def posts(categories, tags):
    posts = [
        Post(title='Test Post 1', text='This is a test post', user_id=1, category=categories[0], tags=[tags[0], tags[1]]),
        Post(title='Test Post 2', text='Another test post', user_id=1, category=categories[1], tags=[tags[1]]),
        Post(title='Test Post 3', text='Yet another test post', user_id=2, category=categories[0], tags=[tags[1], tags[0]])
    ]
    yield posts


@pytest.fixture(scope='module')
def init_database(new_user, posts, categories, tags):

    db.create_all()

    default_user = User(username='Cool User', email='cool@gmail.com', password='password')

    db.session.add_all([new_user, default_user, categories[0], categories[1], tags[0], tags[1], posts[0], posts[1], posts[2]])
    db.session.commit()

    yield


@pytest.fixture(scope='function')
def log_in_default_user(client, new_user):
    client.post(
        url_for('auth.login'),
        data={'email': new_user.email, 'password': 'password'},
        follow_redirects=True
    )

    yield new_user

    client.post(url_for('auth.logout'))