from flask import url_for

from app.post.models import Tag


def test_tags_page_view(client):
    response = client.get(url_for('post.tags'))
    assert response.status_code == 200
    assert b'Tags' in response.data
    
def test_view_all_tags(client, init_database, tags):
    response = client.get(url_for('post.tags'))
    for tag in tags:
        assert tag.name in response.get_data(as_text=True)
    assert response.status_code == 200
    
def test_edit_tags_page_view(client, init_database, log_in_default_user, tags):
    tag = tags[0]
    response = client.get(url_for('post.edit_tag', tag_id=tag.id))
    assert response.status_code == 200
    assert tag.name in response.get_data(as_text=True)
    assert b'Edit tag' in response.data
    
def test_create_tag(client, init_database, log_in_default_user):
    data = {
        'name' : 'Test tag',
    }

    response = client.post(url_for('post.tags'), data=data ,follow_redirects=True)
    
    tag = Tag.query.filter_by(name=data['name']).first()

    assert response.status_code == 200
    assert tag
    assert b'New tag added successfully' in response.data
    
def test_edit_tag(client, init_database, log_in_default_user, tags):
    tag = tags[0]
    data = {
        'name' : 'Edited name',
    }

    response = client.post(url_for('post.edit_tag', tag_id=tag.id), data=data ,follow_redirects=True)
    
    updated = Tag.query.get(tag.id)

    assert response.status_code == 200
    assert updated is not None
    assert updated.title == 'Edited name'
    assert b'Tag has been updated!' in response.data
    
def test_edit_tag(client, init_database, log_in_default_user, tags):
    tag = tags[0]

    response = client.post(url_for('post.delete_tag', tag_id=tag.id), follow_redirects=True)
    
    deleted_tag = Tag.query.filter_by(id=tag.id).first()

    assert response.status_code == 200
    assert deleted_tag is None
    assert b'Tag deleted successfully!' in response.data