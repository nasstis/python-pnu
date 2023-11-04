import json
from flask import Flask
import platform
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.secret_key = 'klchJ89Bch'

os_info = platform.system()
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

with open('users.json') as f:
    users = json.load(f)

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import views