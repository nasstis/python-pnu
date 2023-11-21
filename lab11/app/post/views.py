from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from .models import Post
from .forms import PostForm, EditPostForm
from . import post_blueprint
from .utilities import save_picture
from app import db

@post_blueprint.route('/post/create', methods=['GET', 'POST'])
@login_required
def create():
    form = PostForm()

    if form.validate_on_submit():
        title = form.title.data
        text = form.text.data
        type = form.type.data
        
        if form.image.data:
            image = save_picture(form.image.data)
        else:
            image = 'postdefault.jpg' 
            
        post = Post(title=title, text=text, image=image, type=type, user_id=current_user.id) 
        try:
            db.session.add(post)
            db.session.commit()
            flash('Your post added successfully', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'An error occurred: {str(e)}', 'danger')
        return redirect(url_for("post.create"))
                        
    return render_template("create_post.html", form=form)

@post_blueprint.route('/post', methods=['GET'])
def all_posts():
    posts = Post.query.filter_by(enabled=True).all()

    return render_template('all_posts.html', posts=posts)

@post_blueprint.route('/post/<int:post_id>', methods=['GET'])
def view_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('view_post.html', post=post)

@post_blueprint.route('/post/<int:post_id>/edit', methods=['GET', 'POST'])
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    form = EditPostForm()
    
    if form.validate_on_submit():
        if form.image.data:
            post.image = save_picture(form.image.data)
        try:
            post.title = form.title.data
            post.text = form.text.data
            post.type = form.type.data
            post.enabled = bool(form.enabled.data)
            db.session.commit()
            flash('Post has been updated!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f"Failed to update! Error: {str(e)}", category="danger") 

        return redirect(url_for('post.view_post', post_id=post.id))

    elif request.method == 'GET':
        form.title.data = post.title
        form.text.data = post.text
        form.type.data =  post.type
        form.enabled.data = post.enabled

    return render_template('edit_post.html', post=post, form=form)


@post_blueprint.route('/post/<int:post_id>/delete', methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    
    try:
        db.session.delete(post)
        db.session.commit()
        flash('Post deleted successfully', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'An error occurred: {str(e)}', 'danger')

    return redirect(url_for('post.all_posts'))
