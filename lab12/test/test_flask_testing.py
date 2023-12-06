from flask import Flask, url_for
from flask_login import current_user
from flask_testing import TestCase
from app import create_app
from urllib.request import urlopen
import unittest
from app import db
from app.auth.models import User
from app.todo.models import Todo

class MyTest(TestCase):

    def create_app(self):
        app = create_app('test')
        return app
    
    def setUp(self):
        db.create_all()
        user = User(username='user', email='user@gmail.com', password='password')
        db.session.add(user)
        db.session.commit()
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        
    def test_setup(self):
        self.assertTrue(self.app is not None)
        self.assertTrue(self.client is not None)
        self.assertTrue(self._ctx is not None)
        
    def test_register_user(self):
        user = User.query.filter_by(username='user').first()
        assert user.username == 'user'
        assert user.email == 'user@gmail.com'
        assert user.password_hash != 'password'
        
    def test_register_post(self):
        with self.client:
            response = self.client.post(
                '/register',
                data=dict(username='test', email='test@test.com', password='password', confirm_password='password'),
                follow_redirects=True
            )
            assert response.status_code == 200
            self.assertIn(b'Account successfully created', response.data)
        user = User.query.filter_by(email='test@test.com').first()
        assert user.email == 'test@test.com'
        
    def test_login_user(self):
        with self.client:
            response = self.client.post(
                url_for('auth.login'),
                data=dict(email='user@gmail.com', password='password'),
                follow_redirects=True
            )
            assert response.status_code == 200
            assert current_user.is_authenticated == True
            self.assertIn(b'You have been logged in successfully!', response.data)
            
    def test_todo_create(self):
        # login_user(User.query.filter_by(id=1).first())
        data = {
            'title': 'Write flask tests',  
            'description': 'New description', 
        }
        with self.client:
            response = self.client.post(url_for('todo.add'), data=data, 
                        follow_redirects=True)
            assert response.status_code == 200
            self.assertIn(b'Todo added successfully', response.data)
            
    def test_get_all_todo(self):
        todo1 = Todo(title='todo1', description='description1', complete=False)
        todo2 = Todo(title='todo2', description='description2', complete=False)
        db.session.add_all([todo1, todo2])
        all_todo = Todo.query.count()
        assert all_todo == 2
        
    def test_update_todo_complete(self):
        todo1 = Todo(title='todo1', description='description1', complete=False)
        db.session.add(todo1)
        with self.client:
            response = self.client.get(url_for('todo.update',todo_id=1), follow_redirects=True)
            todo = Todo.query.get(1) #треба забрати get і робити через filter_by
            assert todo.complete == True
    
    def test_view_index(self):  
        url = 'http://localhost:5000/'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Tsapko', response.data)
        
    def test_login_page_loads(self):
        with self.client:
            response = self.client.get(url_for('auth.login'))
            self.assertIn(b'Remember me', response.data)
        
# if __name__ == '__main__':
#     unittest.main()