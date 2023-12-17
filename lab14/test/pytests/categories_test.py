from flask import url_for

from app.post.models import Category


def test_categories_page_view(client):
    response = client.get(url_for('post.categories'))
    assert response.status_code == 200
    assert b'Categories' in response.data
    
def test_view_all_categories(client, init_database, categories):
    response = client.get(url_for('post.categories'))
    for category in categories:
        assert category.name in response.get_data(as_text=True)
    assert response.status_code == 200
    
def test_edit_categories_page_view(client, init_database, log_in_default_user, categories):
    category = categories[0]
    response = client.get(url_for('post.edit_category', category_id=category.id))
    assert response.status_code == 200
    assert category.name in response.get_data(as_text=True)
    assert b'Edit category' in response.data
    
def test_create_category(client, init_database, log_in_default_user):
    data = {
        'name' : 'Test category',
    }

    response = client.post(url_for('post.categories'), data=data ,follow_redirects=True)
    
    category = Category.query.filter_by(name=data['name']).first()

    assert response.status_code == 200
    assert category
    assert b'New category added successfully' in response.data
    
def test_edit_category(client, init_database, log_in_default_user, categories):
    category = categories[0]
    data = {
        'name' : 'Edited name',
    }

    response = client.post(url_for('post.edit_category', category_id=category.id), data=data ,follow_redirects=True)
    
    updated = Category.query.get(category.id)

    assert response.status_code == 200
    assert updated is not None
    assert updated.title == 'Edited name'
    assert b'Category has been updated!' in response.data
    
def test_edit_category(client, init_database, log_in_default_user, categories):
    category = categories[0]

    response = client.post(url_for('post.delete_category', category_id=category.id), follow_redirects=True)
    
    deleted_category = Category.query.filter_by(id=category.id).first()

    assert response.status_code == 200
    assert deleted_category is None
    assert b'Category deleted successfully!' in response.data
    
