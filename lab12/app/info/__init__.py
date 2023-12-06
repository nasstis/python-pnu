from flask import Blueprint

info_blueprint = Blueprint('info', __name__, template_folder="templates/info")

from . import views