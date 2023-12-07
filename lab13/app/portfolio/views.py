from flask import request, render_template
from . import portfolio_blueprint
import platform
from datetime import datetime
from .data import skills

os_info = platform.system()
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

@portfolio_blueprint.route('/')
def index():
    user_agent = request.user_agent
    return render_template('index.html', os_info=os_info, user_agent=user_agent, current_time=current_time)

@portfolio_blueprint.route('/about')
def about():
     return render_template('about.html')


@portfolio_blueprint.route('/skill')
@portfolio_blueprint.route('/skill/<int:idx>')
def skill(idx=None):
    if idx is not None:
        return render_template("skill.html", idx=idx, skills = skills)
    else:
        return render_template("skills.html", skills = skills)

@portfolio_blueprint.route('/contact')
def contact():
    return render_template('contact.html')
