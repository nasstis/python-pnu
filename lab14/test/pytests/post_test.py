from flask import url_for

from app.post.models import Category, Post, Tag

def test_post_page_view(client):
    response = client.get(url_for('post.all_posts'))
    assert response.status_code == 200
    assert b'All posts' in response.data
    
    
def test_post_create_page_view(client):
    response = client.get(url_for('post.create'))
    assert response.status_code == 200
    assert b'Here you can add your post' in response.data
    
    
def test_post_by_id_page_view(client, init_database, posts):
    post = posts[0]

    response = client.get(url_for('post.view_post', post_id=post.id))
    
    assert response.status_code == 200
    assert post.title in response.get_data(as_text=True)
    assert 'Edit' not in response.get_data(as_text=True)
    assert 'Delete' not in response.get_data(as_text=True)
    
def test_post_by_id_page_view_author(client, init_database, posts, log_in_default_user):
    post = posts[0]

    response = client.get(url_for('post.view_post', post_id=post.id))
    
    assert response.status_code == 200
    assert post.title in response.get_data(as_text=True)
    assert 'Edit' in response.get_data(as_text=True)
    assert 'Delete' in response.get_data(as_text=True)
    
def test_post_edit_page_view(client, init_database, log_in_default_user, posts):
    post = posts[0]

    response = client.get(url_for('post.edit_post', post_id=post.id))

    assert response.status_code == 200
    assert post.title in response.get_data(as_text=True)
    assert b'Edit post' in response.data
    
##############################################################################################

def test_create_post(client, init_database, log_in_default_user, categories, tags):
    data = {
        'title': 'New',
        'text': 'Some text',
        'category': categories[0].id,
        'type': 'news',
        'tags': [tags[0].id],
    }

    response = client.post(url_for('post.create'), data=data, follow_redirects=True)
    
    post = Post.query.filter_by(title='New').first()

    assert response.status_code == 200
    assert post
    assert post.user_id == log_in_default_user.id
    assert b'Your post added successfully' in response.data
    
def test_get_all_posts(init_database):
    number_of_posts = Post.query.count()
    assert number_of_posts == 4
    
def test_edit_post(client, init_database, log_in_default_user, categories, tags, posts):
    post_to_update = posts[0]
    data = {
        'title' : 'Edited',
        'text' : post_to_update.text,
        'type' : 'other',
        'enabled' : post_to_update.enabled,
        'category' : post_to_update.category_id,
        'tags' : [tags[0].id, tags[1].id],
    }
        
    response = client.post(url_for('post.edit_post', post_id=post_to_update.id), data=data, follow_redirects=True)
    
    updated = Post.query.get(post_to_update.id)

    assert response.status_code == 200
    assert updated is not None
    assert updated.title == 'Edited'
    assert len(updated.tags) == 2
    assert b'Post has been updated!' in response.data

def test_delete_post(client, init_database, log_in_default_user):
    response = client.post(
        url_for('post.delete_post', post_id=2),
        follow_redirects=True
    )
    deleted_post = Post.query.filter_by(id=2).first()
    assert response.status_code == 200
    assert deleted_post is None
    assert b'Post deleted successfully' in response.data
