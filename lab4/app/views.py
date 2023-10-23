from datetime import datetime, timedelta
import json
from flask import make_response, redirect, render_template, request, session, url_for
from data import skills
from app import app, os_info, current_time, users

@app.route('/')
def index():
    user_agent = request.user_agent
    return render_template('index.html', os_info=os_info, user_agent=user_agent, current_time=current_time)

@app.route('/about')
def about():
     user_agent = request.user_agent
     return render_template('about.html', os_info=os_info, user_agent=user_agent, current_time=current_time)


@app.route('/skill')
@app.route('/skill/<int:idx>')
def skill(idx=None):
    user_agent = request.user_agent
    if idx is not None:
        return render_template("skill.html", idx=idx, os_info=os_info, user_agent=user_agent, current_time=current_time, skills = skills)
    else:
        return render_template("skills.html", os_info=os_info, user_agent=user_agent, current_time=current_time, skills = skills)

@app.route('/contact')
def contact():
    user_agent = request.user_agent
    return render_template('contact.html', os_info=os_info, user_agent=user_agent, current_time=current_time)

@app.route('/info')
def info():
    if 'name' not in session:
        return redirect(url_for('login'))

    user_agent = request.user_agent
    name = session.get('name')

    cookies = request.cookies.items()

    message = request.args.get('message')

    return render_template('info.html', name=name, os_info=os_info, user_agent=user_agent, current_time=current_time, cookies=cookies, message=message)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if 'name' in session:
        return redirect(url_for('info'))

    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
  
        if name in users and users[name] == password:
            session['name'] = name
            return redirect(url_for('info'))
        else:
           return render_template('login.html')
    return render_template('login.html')

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('name', None)
    return redirect(url_for('login'))

@app.route('/add_cookie', methods=['POST'])
def add_cookie():
    key = request.form.get('key')
    value = request.form.get('value')
    expiry = int(request.form.get('expiry'))

    resp = make_response(redirect(url_for('info', message='Cookie added')))

    resp.set_cookie(key, value, max_age=expiry)

    return resp

@app.route('/delete_cookie', methods=['POST'])
def delete_cookie():
    delete_key = request.form.get('delete_key')

    resp = make_response(redirect(url_for('info', message='Cookie deleted')))

    resp.delete_cookie(delete_key)

    return resp

@app.route('/delete_all_cookies', methods=['POST'])
def delete_all_cookies():
    resp = make_response(redirect(url_for('info', message='All cookies deleted')))

    cookies = request.cookies
    for key in cookies.keys():
        resp.delete_cookie(key)

    return resp

@app.route('/change_password', methods=['POST'])
def change_password():
    current_password = request.form['current_password']
    new_password = request.form['new_password']
    confirm_password = request.form['confirm_password']

    if current_password != users[session['name']]:
        message = "Incorrect current password. Please try again."
        return render_template('info.html', name=session.get('name'), message=message)

    if new_password != confirm_password:
        message = "New password and confirmation do not match. Please try again."
        return render_template('info.html', name=session.get('name'), message=message)

    users[session['name']] = new_password
    with open('users.json', 'w') as file:
        json.dump(users, file)

    message = "Password updated successfully."
    return render_template('info.html', name=session.get('name'), message=message)
