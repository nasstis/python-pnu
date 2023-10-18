from flask import Flask, render_template, url_for, request
import platform
from data import skills
from datetime import datetime
app = Flask(__name__)

os_info = platform.system()
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

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

if __name__ == '__main__':
    app.run(debug=True)