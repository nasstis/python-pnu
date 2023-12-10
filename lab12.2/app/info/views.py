from flask import make_response, redirect, render_template, request, url_for, flash
from flask_login import current_user, login_required
from . import info_blueprint

@info_blueprint.route('/info')
@login_required
def info():
    # if 'name' not in session:
    #     flash('Please log in first!', 'danger')
    #     return redirect(url_for('login'))

    name = current_user.username
    cookies = request.cookies.items()

    return render_template('info.html', name=name, cookies=cookies)

@info_blueprint.route('/delete_all_cookies', methods=['POST'])
def delete_all_cookies():
    flash('All cookies deleted!', 'primary')
    resp = make_response(redirect(url_for('info.info')))

    cookies = request.cookies
    for key in cookies.keys():
        resp.delete_cookie(key)

    return resp

@info_blueprint.route('/add_cookie', methods=['POST'])
def add_cookie():
    key = request.form.get('key')
    value = request.form.get('value')
    expiry = int(request.form.get('expiry'))

    flash('Cookie added!', 'primary')
    resp = make_response(redirect(url_for('info.info')))

    resp.set_cookie(key, value, max_age=expiry)

    return resp

@info_blueprint.route('/delete_cookie', methods=['POST'])
def delete_cookie():
    delete_key = request.form.get('delete_key')

    flash('Cookie deleted!', 'primary')
    resp = make_response(redirect(url_for('info.info')))

    resp.delete_cookie(delete_key)

    return resp