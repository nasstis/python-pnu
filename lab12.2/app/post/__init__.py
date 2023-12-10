from flask import Blueprint

post_blueprint = Blueprint('post', __name__, template_folder="templates/post")

from . import views